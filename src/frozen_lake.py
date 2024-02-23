import numpy as np


def add_holes(env):
    n_holes = np.random.randint(0, 4)
    holes = []
    while len(holes) < n_holes:
        hole = (np.random.randint(0, 4), np.random.randint(0, 4))
        if hole not in holes and hole != (0, 0) and hole != (3, 3):  # To avoid placing holes on agent or goal
            holes.append(hole)

    for hole in holes:
        env[hole[0]][hole[1]] = -1

    return env


def start_env():
    env = []
    for i in range(4):
        env.append(np.zeros(4))
    env[0][0] = 1
    env[3][3] = 2
    return add_holes(env)


def print_env(env):
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
    def __init__(self):
        np.random.seed(4)

        # 4x4 grid. Agent on (0, 0) and goal on (3, 3). Holes (max 3) are randomly placed.
        self.env = start_env()
        print_env(self.env)