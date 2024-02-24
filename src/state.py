class State:
    def __init__(self, x, y):
        self.value = (x, y)

    def __repr__(self):
        return f'State{self.value}'

    def __str__(self):
        return f'State{self.value}'

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)