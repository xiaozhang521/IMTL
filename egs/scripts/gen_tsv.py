import yaml
import sys
from pathlib import Path
from itertools import groupby
import torchaudio
import os
import math
#wav_root=Path("/data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/data/tst-COMMON/wav/")
output_prex="/home/zhangyuhao/DATA/mustc-en"+sys.argv[1]+"/test-split/"
#os.system("mkdir -p /data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/data/tst-COMMON-split/")

f=open("./en-ru/data/tst-COMMON/txt/tst-COMMON.yaml","r")
src=open("./en-ru/data/tst-COMMON/txt/tst-COMMON.en","r")
tgt=open("./en-ru/data/tst-COMMON/txt/tst-COMMON.ru","r")
segments = yaml.load(f, Loader=yaml.BaseLoader)
out=open("tst-COMMON.tsv","w")
cot=0
out.write("id\taudio\tn_frames\ttgt_text\tsrc_text\n")
for wav_filename, _seg_group in  groupby(segments, lambda x: x["wav"]):
       #wav_path = wav_root / wav_filename
       #wav_path = wav_root / item["wav"]
       #sample_rate = torchaudio.info(wav_path.as_posix()).sample_rate 
       wav_filename = wav_filename.replace(".wav","")
       seg_group = sorted(_seg_group, key=lambda x: float(x["offset"]))
       for i, segment in enumerate(seg_group):
           s=src.readline()
           t=tgt.readline()
           #offset = int(float(segment["offset"]) * sample_rate)
           n_frames = int(float(segment["duration"]) * 16000)
           frames=int(math.ceil(math.ceil(n_frames*1.0/16) - 20) *1.0/10)
           _id = f"test_{wav_filename}_{i}"
           wav_path=output_prex+_id+".wav" 
           if 5<= frames :
              out.write(_id+"\t"+wav_path+"\t"+str(frames)+"\t"+t.strip()+"\t"+s.lower())
              cot+=1 
print(cot)
           #waveform, _ = torchaudio.load(wav_path, frame_offset=offset, num_frames=n_frames)
           #torchaudio.save(output_prex+_id+'.wav', waveform, sample_rate)
    #seg_group = sorted(_seg_group, key=lambda x: float(x["offset"]))
    #for i, segment in enumerate(seg_group):
    #            offset = int(float(segment["offset"]) * sample_rate)
    #            n_frames = int(float(segment["duration"]) * sample_rate)
    #            _id = f"{split}_{wav_path.stem}_{i}"
    #            self.data.append(
    #                (
    #                    wav_path.as_posix(),
    #                    offset,
    #                    n_frames,
    #                    sample_rate,
    #                    segment["en"],
    #                    segment[lang],
    #                    segment["speaker_id"],
    #                    _id,
    #                )
    #            )
