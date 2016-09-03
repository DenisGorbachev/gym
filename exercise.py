import gym
import registry

env = gym.make('FrozenLakeDeterministic-v0')
observation = env.reset()

# 0 - Left
# 1 - Down
# 2 - Right
# 3 - Up
actions = [
    1, 2, 1, 0,
    1, 7, 1, 7,
    2, 1, 1, 7,
    7, 2, 2, 9,
]

for t in range(10):
    print("========")
    dir(env.action_space)
    env.render()
    print(observation)
    action = actions[observation]  # actions.pop()
    print(action)
    observation, reward, done, info = env.step(action)
    print(info)
    if done:
        print("########")
        env.render()
        print(observation)
        print("Episode finished after {} timesteps".format(t + 1))
        if reward:
            print("Win!")
        else:
            print("Loss!")
        break
