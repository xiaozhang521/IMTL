#fo = open("merge.spm.filter.en","r")
fo = open("mustc.spm.en","r")
words = open("dict.es.txt","r").read().strip().split("\n")

d = [word.split(" ")[0] for word in words] 
d.append("<s>")

cot=0
for line in fo:
    words = line.strip().split(" ")
    for word in words:
        if word not in d:
            print(word)
            #print(line)
    #if " / " in line:
    #    cot+=1

#print(cot)
