import sys
import string
import random
fo=open(sys.argv[1],"r")
fo2=open(sys.argv[2],"r")
#out=open("../mustc.spm.en.lcrm","w")
out1=open(sys.argv[1]+".silent","w")
out2=open(sys.argv[2]+".silent","w")
rm_punk=",.;!?:"
punk=string.punctuation
punk=punk.replace("'","")
for i in rm_punk:
    punk=punk.replace(i,"")

for line,tgt in zip(fo,fo2):
    if len(line.strip().split(" ")) < 120 and len(tgt.strip().split(" ")) < 120:
        line=line.strip()
        if random.random() < 0.2:
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
        #else:
        out1.write(line+"\n")
        out2.write(tgt)

