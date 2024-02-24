import numpy as np

from src.state import State


def print_env(env: list):
    for row in env:
        for col in row:
            if col == 1:  # Agent
                print('☺', end=' ')
            elif col == 2:  # Goal
                print('★', end=' ')
            elif col == -1:  # Hole
                print('▢', end=' ')
            else:  # Empty
                print('▣', end=' ')
        print()


class FrozenLake:
    def __init__(self, env_size: int, n_holes: int, start: tuple, goal: tuple):
        np.random.seed(4)

        self.actions = ['up', 'down', 'left', 'right']
        self.size = env_size
        self.n_holes = n_holes
        self.start = start
        self.goal = goal

        # 4x4 grid. Agent on (0, 0) and goal on (3, 3). Holes (max 3) are randomly placed.
        self.env = self._start_env()

        self.graph = self._create_graph()
        self.states, self.P = self._create_states()
        self.rewards = self._create_rewards()

    def _create_graph(self):
        graph = {}

        for i in range(self.size):
            for j in range(self.size):
                state = State(i, j)
                graph[state] = {}
                for action in self.actions:
                    graph[state][action] = None
                    if action == 'up':
                        if i - 1 >= 0:
                            graph[state][action] = (i - 1, j)
                    elif action == 'down':
                        if i + 1 < self.size:
                            graph[state][action] = (i + 1, j)
                    elif action == 'left':
                        if j - 1 >= 0:
                            graph[state][action] = (i, j - 1)
                    elif action == 'right':
                        if j + 1 < self.size:
                            graph[state][action] = (i, j + 1)

        return graph

    def _create_states(self):
        states = self.graph.keys()
        states = list(states)

        # Create the transition probabilities structure
        probabilities = {}
        for state in states:
            probabilities[state] = {}
            for action in self.actions:
                probabilities[state][action] = {}
                for next_state in states:
                    probabilities[state][action][next_state] = 0

        # Fill the transition probabilities
        for state in states:
            valid_actions = [action for action in self.actions if self.graph[state][action] is not None]
            n_valid_actions = len(valid_actions)
            for action in valid_actions:
                next_state = State(*self.graph[state][action])
                probabilities[state][action][next_state] = 1 / n_valid_actions

        return states, probabilities

    def _create_rewards(self):
        rewards = {}
        for state in self.states:
            rewards[state] = {}
            for action in self.actions:
                # If the action is invalid (hits a wall), penalize the agent
                if self.graph[state][action] is None:
                    rewards[state][action] = -5
                else:
                    next_state = State(*self.graph[state][action])
                    if next_state.value == self.goal:
                        rewards[state][action] = 1000
                    elif next_state.value in self.holes:
                        rewards[state][action] = -1000
                    else:
                        rewards[state][action] = -1
        return rewards

    def _start_env(self):
        env = []
        for i in range(self.size):
            env.append(np.zeros(self.size))
        env[self.start[0]][self.start[1]] = 1
        env[self.goal[0]][self.goal[1]] = 2
        return self._add_holes(env)

    def _add_holes(self, env: list):
        n_holes = np.random.randint(0, self.n_holes + 1)  # Random number of holes
        self.holes = []
        while len(self.holes) < n_holes:
            hole = (np.random.randint(0, self.size), np.random.randint(0, self.size))
            if hole not in self.holes and hole != self.start and hole != self.goal:  # To avoid placing holes on agent or goal
                self.holes.append(hole)

        for hole in self.holes:
            env[hole[0]][hole[1]] = -1

        return env

    def show_policy(self, policy: dict):
        current_state = self.start
        while current_state != self.goal:
            print_env(self.env)
            action = policy[State(*current_state)]
            print(f'Optimal Action: {action}')
            next_state = self.graph[State(*current_state)][action]
            self.env[current_state[0]][current_state[1]] = 0
            self.env[next_state[0]][next_state[1]] = 1
            current_state = next_state
            print('-----------------')
