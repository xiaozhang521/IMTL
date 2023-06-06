import string
import random
fo=open("merge.spm.en","r")
fo2=open("merge.spm.es","r")
out1=open("merge.spm.filter.en","w")
out2=open("merge.spm.filter.es","w")
rm_punk=",.;!?:"
punk=string.punctuation
punk=punk.replace("'","")
for i in rm_punk:
    punk=punk.replace(i,"")

for line,tgt in zip(fo,fo2):
    if len(line.strip().split(" ")) < 150 and len(tgt.strip().split(" ")) < 150:
        if " / " in line:
            line = line.replace(" / "," <s> "
        if random.random() < 0.2:
            line=line.strip()
            #for w in punk:
            #    line = line.replace(w,"")
            line = line.replace("...","<s>")
            line = line.replace("..","<s>")
            for w in rm_punk:
                if w in line:
                    if " "+ w +" " in line:
                        line = line.replace(" "+w+" "," <s> ")
                    elif w == line[-1] and " " == line[-2]:
                        line = line[:-1] + "<s>"
                    elif w == line[0] and " " == line[1]:
                        line = "<s>" + line[1:]
            line=line.replace("  "," ")
            line=line.replace("<s><s>","<s>")
            line=line.replace("▁<s>","<s>")
            #out.write(line)
            #out1.write(line+"\n")
            #out2.write(tgt)
            tags = line.strip().split(" ")
            ratio = random.random()*0.1+0.1
            length = len(tags)
            add_num = round(len(tags) * ratio)
            for i in range(add_num):
                pos = int(random.random() * length)
                while "▁" not in tags[pos]:
                    if pos == length-1:
                        break
                    else:
                        pos+=1
                tags.insert(pos,'<s>')
            line=" ".join(tags)
            out1.write(line+"\n")
            out2.write(tgt)
        else:
            out1.write(line)
            out2.write(tgt)

