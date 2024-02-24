class MarkovDecisionProcess:
    def __init__(self, states: list, actions: list, transitions: dict, rewards: dict):
        self.states = states
        self.actions = actions
        self.transitions = transitions
        self.rewards = rewards
        self.policy = {state: actions[0] for state in states}
        eval_policy = self.evaluate_policy()

    def iterate_policy(self):
        while True:
            old_policy = self.policy.copy()

            V = self.evaluate_policy()

            self.policy = self.improve_policy(V)

            if all(old_policy[state] == self.policy[state] for state in self.states):
                break

    def evaluate_policy(self):
        V = {state: 0 for state in self.states}

        while True:
            old_V = V.copy()

            for state in self.states:
                action = self.policy[state]
                next_states = self.transitions[state][action]
                V[state] = self.rewards[state][action] + sum(
                    self.transitions[state][action][next_state] * old_V[next_state] for next_state in next_states
                )

            if all(old_V[state] == V[state] for state in self.states):
                break

        return V

    def improve_policy(self, V):
        new_policy = self.policy.copy()

        for state in self.states:
            Q = {}
            for action in self.actions:
                next_states = self.transitions[state][action]
                Q[action] = self.rewards[state][action] + sum(
                    self.transitions[state][action][next_state] * V[next_state] for next_state in next_states
                )

            new_policy[state] = max(Q, key=Q.get)

        return new_policy