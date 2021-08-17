import gym
import getch

env = gym.make("Reacher-v2").env

observation = env.reset()
print(env.action_space)
a=0.45
b= 0.45
f=1200
while f > 0:
    env.render()
    keys_pressed = getch.getch()
    if keys_pressed == 'a':
        a=0.15
        b=0
    elif keys_pressed == 'd':
        a =-0.15
        b=0
    elif keys_pressed == 'w':
        b =0.15
        a=0
    elif keys_pressed == 's':
        b =-0.15
        a=0
    else:
        a=0
        b=0

    #print(observation)
    observation, reward, done, info = env.step([b,a])
    f-=1



print(env.action_space.sample())
print(observation)
print(env.observation_space)
