import sys

fo=open(sys.argv[1],"r")
out=open(sys.argv[1]+".lc","w")
for line in fo:
    out.write(line.lower())
