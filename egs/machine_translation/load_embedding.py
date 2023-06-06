import torch
import fairseq
import numpy as np

arg_overrides={}
state = fairseq.checkpoint_utils.load_checkpoint_to_cpu("checkpoints/wmt-en2de/iwslt23-conv-silent-encoder3-conv3/last8.ensemble.pt", arg_overrides)
dicts=open("/mnt/zhangyuhao/fairseq-0.12.3/egs/machine_translation/data-bin/mustc-ende-lc-silent/dict.de.txt","r").read().strip().split("\n")
output=open("pretrain_embeddings_mustc_ende_iwlst_prenorm_encoder3_conv3_prepos_silent","w")
dicts=["<s>","<pad>","</s>","<unk>"]+dicts
output.write(str(len(dicts))+" 512\n")
for key in list(state['model'].keys()):
    if key == "decoder.embed_tokens.weight":
        embedding=state["model"][key].data
        for index in range(len(dicts)):
            output.write(dicts[index].split(" ")[0]+" ")
            feature=embedding[index:index+1,].numpy()
            np.savetxt(output,feature)
        break
