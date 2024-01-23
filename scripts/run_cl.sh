TASK_Sequence=$1
method=$2
#
#if [ $# -gt 1 ]; then
#    method="$2"  # Assign the value of the second argument
#fi

python3 ../run_cl.py --tasks $TASK_Sequence --seed=0 --cl_method $method --group_id=$TASK_Sequence
python3 ../run_cl.py --tasks $TASK_Sequence --seed=1 --cl_method $method --group_id=$TASK_Sequence
python3 ../run_cl.py --tasks $TASK_Sequence --seed=2 --cl_method $method --group_id=$TASK_Sequence

