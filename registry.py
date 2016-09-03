from gym.envs.registration import registry, register, make, spec

register(
    id='FrozenLakeDeterministic-v0',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name' : '4x4', 'is_slippery' : False},
    timestep_limit=100,
    reward_threshold=0.78, # optimum = .8196
)
