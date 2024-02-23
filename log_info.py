import pandas as pd
import numpy as np
import os
from glob import glob
import shutil
import json


def get_info(path):
    pattern = os.path.join(path, '*')  # Create a pattern to match all items in the parent folder
    subfolders = [folder for folder in glob(pattern) if os.path.isdir(folder)]
    for trial in subfolders:
        progress_dir = os.path.join(trial, 'config.json')
        with open(progress_dir, 'r') as file:
            data = json.load(file)
            tasks = data['tasks'] if data['tasks'] is not None else data['task_list']
            cl_method = 'fine_tuning' if data['cl_method'] is None else data['cl_method']
            print('-'*15)
            print(progress_dir)
            print(cl_method)
            print(tasks)
            print(data['seed'])
            print('-' * 15)




path = '/home/ruiqi/projects/continual_world/scripts/logs/CW3_1'
get_info(path)
