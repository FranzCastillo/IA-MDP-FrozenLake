import numpy as np

from src.node import Node


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

        self.size = env_size
        self.n_holes = n_holes
        self.start = start
        self.goal = goal

        # 4x4 grid. Agent on (0, 0) and goal on (3, 3). Holes (max 3) are randomly placed.
        self.env = self._start_env()
        self.graph = self._generate_graph()
        print_env(self.env)

    def _start_env(self):
        env = []
        for i in range(self.size):
            env.append(np.zeros(self.size))
        env[self.start[0]][self.start[1]] = 1
        env[self.goal[0]][self.goal[1]] = 2
        return self._add_holes(env)

    def _add_holes(self, env: list):
        n_holes = np.random.randint(0, self.n_holes + 1)  # Random number of holes
        holes = []
        while len(holes) < n_holes:
            hole = (np.random.randint(0, self.size), np.random.randint(0, self.size))
            if hole not in holes and hole != self.start and hole != self.goal:  # To avoid placing holes on agent or goal
                holes.append(hole)

        for hole in holes:
            env[hole[0]][hole[1]] = -1

        return env

    def _generate_graph(self):
        graph = {}
        for i in range(self.size):
            for j in range(self.size):
                if self.env[i][j] == -1:  # Don't add holes to the graph
                    continue

                node = Node((i, j))
                graph[node] = {}

                if i > 0 and self.env[i - 1][j] != -1:  # Up
                    graph[node]["up"] = Node((i - 1, j))
                if i < self.size - 1 and self.env[i + 1][j] != -1:
                    graph[node]["down"] = Node((i + 1, j))
                if j > 0 and self.env[i][j - 1] != -1:
                    graph[node]["left"] = Node((i, j - 1))
                if j < self.size - 1 and self.env[i][j + 1] != -1:
                    graph[node]["right"] = Node((i, j + 1))

        return graph
