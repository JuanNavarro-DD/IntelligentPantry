import gym


env = gym.make("Reacher-v2").env

observation = env.reset()

for _ in range(500):
    env.render()
    print(observation)
    observation, reward, done, info = env.step(env.action_space.sample())
    


print(env.action_space)
print(env.observation_space)
