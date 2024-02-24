class State:
    def __init__(self, value: tuple):
        self.value = value
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)

    def __repr__(self):
        return f'State{self.value}'

    def __str__(self):
        return f'State{self.value}'

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)