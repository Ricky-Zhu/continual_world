from continualworld.envs import get_cl_env, get_single_meta_world_env
import numpy as np

tasks = 'push-v1'
train_env=get_single_meta_world_env(tasks)

max_episode_steps=200

train_env.reset()
for i in range(1001):
    next_obs, reward, done, info=train_env.step(train_env.action_space.sample())
    if done:
        train_env.reset()
        print(i)

success_list = train_env.pop_successes() # this will pop out a list a whether succeed for each episode
print(success_list)
suc_rate=np.mean(success_list)
print(suc_rate)