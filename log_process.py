import pandas as pd
import numpy as np
import os
from glob import glob
import shutil


def remove_incomplete_trials(path):
    pattern = os.path.join(path, '*')  # Create a pattern to match all items in the parent folder
    subfolders = [folder for folder in glob(pattern) if os.path.isdir(folder)]
    for trial in subfolders:
        progress_dir = os.path.join(trial, 'progress.tsv')
        print(trial)
        try:
            data = pd.read_csv(progress_dir, sep='\t')
            if int(max(data['total_env_steps'])) < 900000:
                shutil.rmtree(trial)
        except:
            shutil.rmtree(trial)


path = '/home/ruiqi/projects/continual_world/scripts/logs/2_tasks'
remove_incomplete_trials(path)
