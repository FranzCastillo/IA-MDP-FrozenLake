class MarkovDecisionProcess:
    def __init__(self, states: set, actions: set, transitions: dict, rewards: dict):
        self.states = states
        self.actions = actions
        self.transitions = transitions
        self.rewards = rewards