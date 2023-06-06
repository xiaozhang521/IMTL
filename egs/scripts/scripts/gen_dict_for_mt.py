import sys
fo=open(sys.argv[1]+"/all.spm","r")
dict=open(sys.argv[1]+"/share.dict","w")
d={}
for line in fo:
    words = line.strip().split(" ")
    for word in words:
        if word not in d.keys():
            d[word]=1
        else:
            d[word]+=1
d=sorted(d.items(),key=lambda x:x[1],reverse=True)
for item in d:
    dict.write(item[0]+" " +str(item[1])+"\n")
