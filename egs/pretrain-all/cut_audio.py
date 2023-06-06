import yaml
import sys
from pathlib import Path
from itertools import groupby
import torchaudio
wav_root=Path("/mnt/zhangyuhao/Tibet/dev/wav")
output_prex="/mnt/zhangyuhao/Tibet/dev/wav-split/"
y=open("/mnt/zhangyuhao/Tibet/dev/txt/dev.yaml","r")
src =open("/mnt/zhangyuhao/Tibet/dev/txt/dev.tok.ti","r")
tokens=src.read().strip().split("\n")
cot=0
output_tsv="/mnt/zhangyuhao/Tibet/dev.tsv"
out=open(output_tsv,"w")
out.write("id\taudio\tn_frames\ttgt_text\tsrc_text\n")
segments = yaml.load(y, Loader=yaml.BaseLoader)
for wav_filename, _seg_group in  groupby(segments, lambda x: x["wav"]):
       wav_path = wav_root / wav_filename
       #wav_path = wav_root / item["wav"]
       sample_rate = torchaudio.info(wav_path.as_posix()).sample_rate 
       seg_group = sorted(_seg_group, key=lambda x: float(x["offset"]))
       for i, segment in enumerate(seg_group):
           offset = int(float(segment["offset"]) * sample_rate)
           n_frames = int(float(segment["duration"]) * sample_rate)
           _id = f"{wav_path.stem}_{i}"
           waveform, _ = torchaudio.load(wav_path, frame_offset=offset, num_frames=n_frames)
           torchaudio.save(output_prex+_id+'.wav', waveform, sample_rate)
           out.write(_id+"\t"+output_prex+_id+'.wav'+"\t"+str(n_frames)+"\t"+tokens[cot]+"\t"+tokens[cot]+"\n")
           cot+=1
           
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
