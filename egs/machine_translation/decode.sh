#!/usr/bin/bash
set -e

model_root_dir=checkpoints
root=
# set task
task=wmt-en2de
# set tag

model_dir_tag=
data_dir=
model_dir=$model_root_dir/$task/$model_dir_tag



checkpoint=


ensemble=8

gpu=5

if [ -n "$ensemble" ]; then
        if [ ! -e "$model_dir/last$ensemble.ensemble.pt" ]; then
                PYTHONPATH=`pwd` python3 $root/scripts/average_checkpoints.py --inputs $model_dir --output $model_dir/last$ensemble.ensemble.pt --num-epoch-checkpoints $ensemble
        fi
        checkpoint=last$ensemble.ensemble.pt
fi

output=$model_dir/translation.log

if [ -n "$cpu" ]; then
        use_cpu=--cpu
fi

export CUDA_VISIBLE_DEVICES=$gpu

python3 $root/fairseq_cli/generate.py \
data-bin/$data_dir \
--path $model_dir/$checkpoint \
--gen-subset test \
--batch-size 32 \
--lenpen 1.0 \
--max-source-positions 500 \
--scoring sacrebleu \
--source-lang en \
--target-lang de \
--beam 6 \
--remove-bpe sentencepiece \
--results-path ${model_dir} 

tail -n3  $model_dir/generate-test.txt

