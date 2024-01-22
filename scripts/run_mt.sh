TASK_Sequence=$@

python3 run_mt.py --task_list $TASK_Sequence --seed=0 --group_id=mt
python3 run_mt.py --task_list $TASK_Sequence --seed=1 --group_id=mt
python3 run_mt.py --task_list $TASK_Sequence --seed=2 --group_id=mt
