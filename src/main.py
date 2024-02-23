from src.frozen_lake import FrozenLake


def main():
    env_size = 4
    n_holes = 3
    start = (0, 0)
    goal = (3, 3)

    fl = FrozenLake(env_size, n_holes, start, goal)


if __name__ == "__main__":
    main()
