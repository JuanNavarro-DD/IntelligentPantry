import gym
from gym.wrappers.monitoring import video_recorder


def main():
    env = gym.make('MountainCar-v0')

    env = gym.wrappers.Monitor(env,'.',force=True)

    for episode in range(100):
        env.reset()
         
        while True:
            env.render()
            action =env.action_space.sample()
            obs,reward, don, info = env.step(action)


if __name__ == '__main__':
    main()