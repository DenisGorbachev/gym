import gym
import registry


action_names = ["Left", "Down", "Right", "Up"]

# env = gym.make('FrozenLakeDeterministic-v0')
# actions = [
#     1, 2, 1, 0,
#     1, 7, 1, 7,
#     2, 1, 1, 7,
#     7, 2, 2, 9,
# ]

env = gym.make('FrozenLake-v0')
actions = [
    0, 3, 3, 3,
    0, 7, 0, 7,
    3, 1, 0, 7,
    7, 2, 1, 9,
]

total_reward = 0
max_episodes = 500

for episode in range(max_episodes):
    print("==== Begin Episode {} ====".format(episode))
    observation = env.reset()
    done = False
    steps = 0
    while not done:
        # env.render()
        action = actions[observation]  # actions.pop()
        # print("-> {}".format(action_names[action]))
        observation, reward, done, info = env.step(action)
        steps += 1
    # env.render()
    print("#### End Episode {} after {} steps ####".format(episode, steps))
    total_reward += reward
    if reward:
        print("Win!")
    else:
        print("Loss!")
        # break

print("Total reward: {} / {} @ {}".format(total_reward, max_episodes, total_reward / max_episodes))
