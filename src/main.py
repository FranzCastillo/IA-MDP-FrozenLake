from src.frozen_lake import FrozenLake
from src.mdp import MarkovDecisionProcess


def main():
    env_size = 4
    n_holes = 3
    start = (0, 0)
    goal = (3, 3)

    world = FrozenLake(env_size, n_holes, start, goal)

    states = world.states
    actions = world.actions
    P = world.P
    R = world.rewards

    mdp = MarkovDecisionProcess(states, actions, P, R)

    mdp.iterate_policy()

    optimal_policy = mdp.policy
    print(optimal_policy)


if __name__ == "__main__":
    main()
