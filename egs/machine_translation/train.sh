#! /usr/bin/bash
set -e

device=2,3



task=wmt-en2de
# must set this tag

tag=


if [ $task == "wmt-en2de" ]; then
        arch="transformer_mustc_en_de_encoder3_conv3"
        share_embedding=1
        share_decoder_input_output_embed=1
        criterion=label_smoothed_cross_entropy
        fp16=1
        lr=0.001
        warmup=4000
        max_tokens=4096
        update_freq=1
        weight_decay=0.0
        keep_last_epochs=10
        max_epoch=28
        max_update=
        reset_optimizer=0
        data_dir=mustc-ende-lc-silent
        src_lang=en
        tgt_lang=de
elif [ $task == "wmt-en2fr" ]; then
        #arch=transformer_iwslt_de_en
        arch=transformer_mustc_en_de
        share_embedding=1
        share_decoder_input_output_embed=1
        criterion=label_smoothed_cross_entropy
        fp16=1
        lr=0.001
        warmup=4000
        max_tokens=4096
        update_freq=1
        weight_decay=0.0
        keep_last_epochs=10
        max_epoch=25
        max_update=
        reset_optimizer=0
        data_dir=mustc-enfr-lc
        src_lang=en
        tgt_lang=fr
elif [ $task == "wmt-en2zh" ]; then
        arch=transformer_deep_enzh_768_conv
        share_embedding=0
        share_decoder_input_output_embed=1
        criterion=label_smoothed_cross_entropy
        fp16=1
        lr=0.002
        warmup=16000
        max_tokens=8192
        update_freq=1
        weight_decay=0.0
        keep_last_epochs=10
        max_epoch=25
        max_update=
        reset_optimizer=0
        data_dir=iwslt23-enzh
        src_lang=en
        tgt_lang=zh
else
        echo "unknown task=$task"
        exit
fi

save_dir=checkpoints/$task/$tag

if [ ! -d $save_dir ]; then
        mkdir -p $save_dir
fi
cp ${BASH_SOURCE[0]} $save_dir/train.sh

gpu_num=`echo "$device" | awk '{split($0,arr,",");print length(arr)}'`

cmd="python3 -u fairseq-0.12.3/train.py data-bin/$data_dir
  --distributed-world-size $gpu_num -s $src_lang -t $tgt_lang
  --arch $arch
  --optimizer adam --clip-norm 0.0
  --lr-scheduler inverse_sqrt --warmup-init-lr 1e-07 --warmup-updates $warmup
  --lr $lr 
  --weight-decay $weight_decay
  --criterion $criterion --label-smoothing 0.1
  --max-tokens $max_tokens
  --update-freq $update_freq
  --no-progress-bar
  --log-interval 100
  --ddp-backend no_c10d
  --seed 1
  --task translation
  --save-dir $save_dir
  --keep-last-epochs $keep_last_epochs
  --tensorboard-logdir $save_dir"


adam_betas="'(0.9, 0.997)'"
cmd=${cmd}" --adam-betas "${adam_betas}
if [ $share_embedding -eq 1 ]; then
cmd=${cmd}" --share-all-embeddings "
fi
if [ $share_decoder_input_output_embed -eq 1 ]; then
cmd=${cmd}" --share-decoder-input-output-embed "
fi
if [ -n "$max_epoch" ]; then
cmd=${cmd}" --max-epoch "${max_epoch}
fi
if [ -n "$max_update" ]; then
cmd=${cmd}" --max-update "${max_update}
fi
if [ -n "$dropout" ]; then
cmd=${cmd}" --dropout "${dropout}
fi
if [ $fp16 -eq 1 ]; then
cmd=${cmd}" --fp16 "
fi
if [ $reset_optimizer -eq 1 ]; then
cmd=${cmd}" --reset-optimizer "
fi

#echo $cmd
#eval $cmd
#cmd=$(eval $cmd)
#nohup $cmd exec 1> $save_dir/train.log exec 2>&1 &
#tail -f $save_dir/train.log

export CUDA_VISIBLE_DEVICES=$device
cmd="nohup "${cmd}" > $save_dir/train.log 2>&1 &"
eval $cmd
tail -f $save_dir/train.log

