TASK_SEQS = {
    "CW10": [
        "hammer-v1",
        "push-wall-v1",
        "faucet-close-v1",
        "push-back-v1",
        "stick-pull-v1",
        "handle-press-side-v1",
        "push-v1",
        "shelf-place-v1",
        "window-close-v1",
        "peg-unplug-side-v1",
    ],
}

TASK_SEQS["CW20"] = TASK_SEQS["CW10"] + TASK_SEQS["CW10"]

# triplet task sequence (A->B->C) in which A->C has large positive transfer than B->C
TASK_SEQS["CW3_1"] = ['push-v1', 'window-close-v1', 'hammer-v1']
TASK_SEQS["CW3_5"] = ["faucet-close-v1", 'shelf-place-v1', "push-back-v1"]
TASK_SEQS["CW3_6"] = ['stick-pull-v1', 'peg-unplug-side-v1', 'stick-pull-v1']
TASK_SEQS["CW3_8"] = ['faucet-close-v1', 'shelf-place-v1', 'peg-unplug-side-v1']
