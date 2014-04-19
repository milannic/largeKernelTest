import sys
import shutil
import os
import re

prefix="./struc_dir/"
struct_list = ["GR","GRW","PST","SEM1","SEM2","SEM3"]
set_list = ["full"]
sym_list = ["asym","sym"]
ele_list = ["al","am","label"]

file_des_list = []

for structure in struct_list:
    os.mkdir(prefix+structure)
    file_des = open(prefix+structure+"/data","w")
    file_des_list.append(file_des)
    for single_set in set_list:
        os.mkdir(prefix+structure+"/"+single_set)
        for sym in sym_list:
            os.mkdir(prefix+structure+"/"+single_set+"/"+sym)
            for ele in ele_list:
                os.mkdir(prefix+structure+"/"+single_set+"/"+sym+"/"+ele+"_"+sym)
fi = open('./data', "r")
struct_tag_des = open('./struct_tag_full','w')

count = 0

for line in fi :
    if count==0:
        train_num = int(line.replace(" ",""))
    elif count==1:
        test_num = int(line.replace(" ",""))
    else:
        a = re.split('\|..\|',line)
        a[0] = a[0].replace('\\t','')
        struct_tag_des.write(a[0]+"\n")
        for index in range(len(struct_list)):
            file_des_list[index].write(a[0]+" |BT| "+a[index+1].lower()+'|ET||EV|\n')
    count = count+1
