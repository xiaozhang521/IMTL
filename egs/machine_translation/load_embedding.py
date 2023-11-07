import torch
import fairseq
import numpy as np

arg_overrides={}
state = fairseq.checkpoint_utils.load_checkpoint_to_cpu("", arg_overrides)
dicts=open("","r").read().strip().split("\n")
output=open("","w")
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
