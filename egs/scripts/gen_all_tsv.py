import sys
import copy
fo = open("en-"+sys.argv[1]+"/train_st.tsv","r")
st = open("en-"+sys.argv[1]+"/data_all_en"+sys.argv[1]+"_lcrm/train_st.tsv","w")
mt = open("en-"+sys.argv[1]+"/data_all_en"+sys.argv[1]+"_lcrm/train_mt.tsv","w")
asr = open("en-"+sys.argv[1]+"/data_all_en"+sys.argv[1]+"_lcrm/train_asr.tsv","w")
head=fo.readline()
st.write(head)
mt.write(head)
asr.write(head)

for line in fo:
    tags=line.strip().split("\t")
    tags[5]=tags[5].lower()
    new_st = '\t'.join(tags)+"\n"
    st.write(new_st)
    asr_tags = copy.deepcopy(tags)
    asr_tags[3] = asr_tags[5]
    new_asr = '\t'.join(asr_tags)+"\n"
    asr.write(new_asr)
    tags[0]=tags[1]=tags[2]=tags[4]=""
    new_mt = '\t'.join(tags)+"\n"
    mt.write(new_mt)
