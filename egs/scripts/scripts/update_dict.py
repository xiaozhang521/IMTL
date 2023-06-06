import sys
fo1 = open("/data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/mustc-silent/share.dict","r")
fo2 = open("/data/xuchen/zyh/must-data/en-"+sys.argv[1]+"/data_all_en"+sys.argv[1]+"_lcrm/dict.out","w")

for line in fo1:
    tags=line.split(" ")
    fo2.write(tags[0]+" 1\n")
