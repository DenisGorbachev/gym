import gym
import registry

field = [
    "Start", "Frozen", "Frozen", "Frozen",
    "Frozen", "Hole", "Frozen", "Hole",
    "Frozen", "Frozen", "Frozen", "Hole",
    "Hole", "Frozen", "Frozen", "Goal",
]

action_names = ["Left", "Down", "Right", "Up"]

# env = gym.make('FrozenLakeDeterministic-v0')
# actions = [
#     "Down", "Right", "Down", "Left",
#     "Down", "None", "Down", "None",
#     "Right", "Down", "Down", "None",
#     "None", "Right", "Right", "None",
# ]

env = gym.make('FrozenLake-v0')
actions = [
    "Left", "Up", "Up", "Up",
    "Left", "None", "Left", "None",
    "Up", "Down", "Left", "None",
    "None", "Right", "Down", "None",
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
        action_name = actions[observation]  # actions.pop()
        action = action_names.index(action_name)
        # print("-> {}".format(action_name))
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
