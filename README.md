# IMTL (Improved Multi-Task Learning for End-to-end Speech Translation)

This is the source code of paper [Rethinking and Improving Multi-task Learning for End-to-end Speech Translation].

The code is forked from `Fairseq-v0.12.2`, please refer to [`Fairseq`](https://github.com/facebookresearch/fairseq/tree/v0.12.2#requirements-and-installation) for more Installation details.

## Useage

The training scripts and configurations on `MuST-C` data-set are listed following:
```
egs
|---machone_translation
|       |---train.sh
|       |---decode.sh
|       |---load_embedding.py
|---pretrain-all
|       |---decode.sh
|       |---device_run.sh
|       |---joint_train.sh

More details are coming soon.