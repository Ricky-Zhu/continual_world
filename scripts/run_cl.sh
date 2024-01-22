TASK_Sequence=$@

python3 ../run_cl.py --tasks $TASK_Sequence --seed=0 --group_id=$TASK_Sequence
python3 ../run_cl.py --tasks $TASK_Sequence --seed=1 --group_id=$TASK_Sequence
python3 ../run_cl.py --tasks $TASK_Sequence --seed=2 --group_id=$TASK_Sequence

