import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import argparse
import os
import gym

SHARD_SIZE = 2000
np_load_old = np.load

np.load = lambda *a,**k: np_load_old(*a,allow_pickle=True,**k)

def get_options():
    parser =argparse.ArgumentParser(description='Clone some expert data..')
    parser.add_argument('bc_data',type = str, help = "The main datastore for this particular expert.")

    args = parser.parse_args()
    return args

def process_data(bc_data_dir):
    """
    Runs training for the agent
    """
    # Load the file store
    states, actions = [],[]
    shards = [x for x in os.listdir(bc_data_dir) if x.endswith('.npy')]
    print("Processing shards: {}".format(shards))

    for shard in shards:
        shard_path = os.path.join(bc_data_dir, shard)
        with open(shard_path,'rb') as f:
            data = np.load(f)
            shard_states, unprocessed_actions = zip(*data)
            shard_states = [x.flatten() for x in shard_states]

            # Add the Shard to the dataset
            states.extend(shard_states)
            actions.extend(unprocessed_actions)

        states = np.asarray(states,dtype = np.float32)
        actions = np.asarray(actions,dtype = np.float32)/2
        print("Processed with {} pairs".format(len(states)))
        return states,actions


def create_model():
    state_ph = tf.placeholder(dtype=tf.float32, shape=[None,2])

    with tf.variable_scope("layer1"):
        hidden_layer = tf.layers.dense(state_ph,128,activation = tf.nn.relu)
    with tf.variable_scope("layer2"):
        hidden_2 = tf.layers.dense(hidden_layer,128, activation = tf.nn.relu)
    with tf.variable_scope("layer3"):
        logits = tf.layers.dense(hidden_2,2)
    with tf.variable_scope("output"):
        action = tf.argmax(input=logits, axis=1)

    return state_ph, action, logits

def create_traning(logits):
    label_ph = tf.placeholder(dtype=tf.int32, shape=[None])

    #Conver to onehot
    with tf.variable_scope("loss"):
        onehot_labels = tf.one_hot(indices=tf.cast(label_ph,tf.int32),depth=2)

        loss = tf.losses.softmax_cross_entropy(onehot_labels=onehot_labels,logits=logits)
        loss = tf.reduce_mean(loss)

        tf.summary.scalar('loss',loss)
    
    with tf.variable_scope("training"):
        optimizer = tf.train.AdamOptimizer(learning_rate=1e-3)
        train_op = optimizer.minimize(loss)

    return train_op, loss, label_ph

def run_main(opts):
    state_data, action_data = process_data(opts.bc_data)

    env = gym.make('MountainCar-v0')
    env._max_episode_step = 1200

    x, model, logits =create_model()
    train, loss, labels =create_traning(logits)

    sess = tf.Session()
    

    #Create summaries
    merged = tf.summary.merge_all()
    train_writer = tf.summary.FileWriter('./logs',sess.graph)
    
    sess.run(tf.global_variables_initializer())
    
    tick = 0

    while True:
        done =False
        obs = env.reset()
        while not done:
            env.render()
            batch_index = np.random.choice(len(state_data),64)
            state_batch, action_batch = state_data[batch_index], action_data[batch_index]

            _, cur_loss, cur_summaries = sess.run([train,loss,merged],feed_dict={x: state_batch,labels: action_batch})

            print("loss: {}".format(cur_loss))
            train_writer.add_summary(cur_summaries,tick)
            action = sess.run(model,feed_dict={x:[obs.flatten()]})[0]*2
        obs, reward, done, info = env.step(action)
        tick+=1

if __name__ == "__main__":
    opts = get_options()

    run_main(opts)

#np.load = np_load_old