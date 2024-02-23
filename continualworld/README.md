## get the CRL training env 
```
train_env = get_cl_env(tasks, steps_per_task)
```

<span style="color:red;">task: str, look at task.py for the definition</span>

<span style="color:red;">steps_per_task: the maximum training steps for each task</span>

### functionality
After given task argument, the class will know the number of tasks in total.
Once it reaches the maximum training steps for one task, it will automatically proceed to next task.
