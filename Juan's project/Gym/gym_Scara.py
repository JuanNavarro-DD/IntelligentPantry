import gym
import getch
import os
from stable_baselines3 import PPO
from stable_baselines3 import DDPG
from stable_baselines3 import TD3
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.evaluation import evaluate_policy

env = gym.make("IntelligentPantry-v1")
#env = gym.make("Reacher-v2")

observation = env.reset()
print(env.action_space)
a = 0.45
b = 0.45
f = 1200
log_path = os.path.join('training', 'Logs')
#env = DummyVecEnv([lambda: env])
model3 = TD3("MlpPolicy", env, verbose=1)
#model2 = DDPG('MlpPolicy',env,verbose=1,tensorboard_log=log_path)
model3.learn(total_timesteps=500000, log_interval=10)
eval = evaluate_policy(model3, env, n_eval_episodes=20, render=True)
# episodes = 5
# for episode in range(1, episodes+1):
#     state = env.reset()
#     done = False
#     score = 0
#
#     while not done:
#         env.render()
#         action = env.action_space.sample()
#         n_state, reward, done, info = env.step(action)
#         score += reward
#     print("Episode:{} Score:{}".format(episode, score))
# env.close()

# while f > 0:
#     env.render()
#     keys_pressed = getch.getch()
#     if keys_pressed == 'a':
#         a=0.15
#         b=0
#     elif keys_pressed == 'd':
#         a =-0.15
#         b=0
#     elif keys_pressed == 'w':
#         b =0.15
#         a=0
#     elif keys_pressed == 's':
#         b =-0.15
#         a=0
#     else:
#         a=0
#         b=0
#
#     #print(observation)
#     observation, reward, done, info = env.step([b,a])
#     f-=1

print("evaluation: ", eval)
print(env.action_space.sample())
print(observation)
print(env.observation_space)
