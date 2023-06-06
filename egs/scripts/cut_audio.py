import yaml
import sys
from pathlib import Path
from itertools import groupby
import torchaudio
import os
wav_root=Path("/data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/data/train/wav/")
output_prex="/data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/data/train-split/"
os.system("mkdir -p /data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/data/train-split/")
f=open(str(wav_root)+"/../txt/train.yaml","r")
segments = yaml.load(f, Loader=yaml.BaseLoader)
for wav_filename, _seg_group in  groupby(segments, lambda x: x["wav"]):
       wav_path = wav_root / wav_filename
       #wav_path = wav_root / item["wav"]
       sample_rate = torchaudio.info(wav_path.as_posix()).sample_rate 
       seg_group = sorted(_seg_group, key=lambda x: float(x["offset"]))
       for i, segment in enumerate(seg_group):
           offset = int(float(segment["offset"]) * sample_rate)
           n_frames = int(float(segment["duration"]) * sample_rate)
           _id = f"train_{wav_path.stem}_{i}"
           waveform, _ = torchaudio.load(wav_path, frame_offset=offset, num_frames=n_frames)
           torchaudio.save(output_prex+_id+'.wav', waveform, sample_rate)
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
