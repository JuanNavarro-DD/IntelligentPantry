'''

Author: Juan Navarro
This code trains an agent in a modified reacher_WSU using keras agents
it aims to train different agents and compare its performance

'''





import gym
import random
import numpy as np
# To build my model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.optimizers import Adam
# To train the model
from rl.agents import DQNAgent
from rl.policy import BoltzmannQPolicy
from rl.memory import SequentialMemory


env = gym.make("Reacher-v2") # The environment has been changed
states = env.observation_space.shape[0]
actions = env.action_space.shape[0]

episodes = 10

# for episode in range(1,episodes+1):
#     state = env.reset()
#     done =False
#     score = 0
#     while not done:
#         env.render()
#         action = random.choice([0,1])
#         m_state, reward, done, info = env.step(action)
#         print(m_state,reward,done,info)
#         score+=reward
#     print('episode {} score: {}'.format(episode,score))

def build_model(states, actions):
    model = Sequential()
    model.add(Flatten(input_shape=(1,states)))
    model.add(Dense(48,activation="relu"))
    model.add(Dense(48,activation="relu"))
    model.add(Dense(actions,activation="linear"))
    return model

def build_agent(model,actions):
    policy = BoltzmannQPolicy()
    memory = SequentialMemory(limit=100000,window_length=1)
    dqn = DQNAgent(model=model, memory=memory, policy=policy, nb_actions=actions,
                    nb_steps_warmup=20, target_model_update = 1e-2)
    return dqn




print(env.reward_range[0])

model = build_model(states,actions)

#dqn = build_agent(model, actions)
#dqn.compile(Adam(lr = 1e-3),metrics =['mae'])
#dqn.fit(env,nb_steps=100000,visualize=False,verbose=1)

#scores = dqn.test(env, nb_episodes = 100, visualize = False)
#print(np.mean(scores.history['episode_reward']))


#print(model.summary())

#dqn._weights('dqn_weights.h5f',overwrite=True) # This is to save the weights of the agent
# To rebuild the model
'''
env = gym.make('Reacher-v2')
states = env.observation_space.shape[0]
actions = env.action_space.shape
model = build_model(states,actions)
dqn = build_agent(model, actions)

#To load the weights we load the file saved above
dqn.loaf_weights('dqn_weights.h5f')
'''
