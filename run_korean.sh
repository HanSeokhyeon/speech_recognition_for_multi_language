#!/bin/sh

export CUDA_VISIBLE_DEVICES="0"

BATCH_SIZE=16
WORKER_SIZE=4
MAX_EPOCHS=1000

python ./run_korean.py --batch_size $BATCH_SIZE --workers $WORKER_SIZE --use_attention --max_epochs $MAX_EPOCHS --bidirectional
