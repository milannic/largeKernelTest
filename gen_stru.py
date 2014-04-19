import sys
import shutil
import os
import re

prefix="./struc_dir/"
struct_list = ["GR","GRW","PST","SEM1","SEM2","SEM3"]
set_list = ["full"]
sym_list = ["asym","sym"]
ele_list = ["al","am","label"]

fold_num = str(sys.argv[1])

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
matlab_template = open("../../../resources/load_data.m","r")
all_template = matlab_template.readlines()
matlab_template.close()
length = train_num+test_num

template="""#PBS -W group_list=yeticcls
#PBS -l nodes=1,walltime=10:00:00,mem=8gb
#PBS -M cl3173@columbia.edu 
#PBS -m abe 
#PBS -V 
# Set output and error directories 
#PBS -o localhost:/vega/ccls/users/cl3173/ 
#PBS -e localhost:/vega/ccls/users/cl3173/ \n"""

time_consuming_kernel = ["PT","SST"]
structure_list=["S1","S2"]


for structure in struct_list:
    matlab_load=open(prefix+structure+"/full/load_data.m",'w')
    matlab_load.write("length=%s\n"%(str(length)))
    for each_line in all_template:
        matlab_load.write(each_line)
    name1 = structure+"_full_data_asym_fold_%s"%(fold_num)
    name2 = structure+"_full_data_sym_fold_%s"%(fold_num)
    name3 = structure+"_S2_full_data_asym_fold_%s"%(fold_num)
    name4 = structure+"_S2_full_data_sym_fold_%s"%(fold_num)
    matlab_load.write(name1+"=my_tr_data_asym;\n")
    matlab_load.write(name2+"=my_tr_data_sym;\n")
    matlab_load.write(name3+"=my_tr_data_asym_s2;\n")
    matlab_load.write(name4+"=my_tr_data_sym_s2;\n")
    matlab_load.write("save(\'../../../../../../folds_data/fold_"+str(fold_num)+"/"+structure+"/full/struct.mat\',\'"+name1+"\',\'"+name2+"\',\'"+name3+"\',\'"+name4+"\');\n")

    for kernel in time_consuming_kernel:
        for s2 in structure_list:
            file_name = "gen_"+kernel+"_"+s2
            name = file_name + "_fold_" +str(fold_num)
            sh_file_des = open(prefix+structure+"/full/%s.sh"%(file_name),'w')
            sh_file_des.write("#! /bin/sh\n#directives\n#PBS -N EXP%s\n"%(name))
            sh_file_des.write(template)
            #sh_file_des.write("cd "+full_path+'/'+dir_prefix+"/%s\n\n"%(ins))
            sh_file_des.write("matlab -nojvm -nodisplay -nosplash -r \"run(\'"+file_name+".m\');quit\" > EXP%s\n"%(name))
            m_file_dex = open(prefix+structure+"/full/%s.m"%(file_name),'w')
            m_file_dex.write("addpath(genpath(\'../../../../graph_kernel\'));\n")
            m_file_dex.write("load(\'struct.mat\');\n")
            tree_kernel_name = "treeKernel"
            kernel_base_name = structure
            struct_name = name1
            if s2 =="S2":
                tree_kernel_name = tree_kernel_name +"_S2"
                kernel_base_name = kernel_name+"_S2"
                struct_name = name3 
            #we also calculate sp with PT
            if kernel == "PT":
                kernel_name2 = kernel_base_name+"_SP_fold_"+str(fold_num)
                m_file_dex.write(kernel_name2+"=spkernel("+struct_name+");\n")
                m_file_dex.write(kernel_name2+"=normalizekm("+kernel_name2+");\n")
            elif kernel == "SST":
                kernel_name2 = kernel_base_name+"_WL_fold_"+str(fold_num)
                m_file_dex.write(kernel_name2+"=WL("+struct_name+",30,1);\n")
                m_file_dex.write(kernel_name2+"="+kernel_name2+"{31};\n")
                m_file_dex.write(kernel_name2+"=normalizekm("+kernel_name2+");\n")
            kernel_name = kernel_base_name+"_"+kernel+"_4_fold_"+str(fold_num)
            if kernel == "PT":
                m_file_dex.write(kernel_name+"="+tree_kernel_name+"("+struct_name+",1,0.4,0.4,0.16,0,0);\n")
            elif kernel == "SST":
                m_file_dex.write(kernel_name+"="+tree_kernel_name+"("+struct_name+",0,0.4,0.4,0.16,0,0);\n")
            m_file_dex.write(kernel_name+"=normalizekm("+kernel_name+");\n")
            m_file_dex.write("save(\'"+kernel_name+".mat\',\'"+kernel_name+"\',\'"+kernel_name2+"\');\n")


#normalizekm
#GR_PT_kernel=treeKernel(GR_full_data_asym,1,1,1,1,0,0);
#GR_PT_kernel_4=treeKernel(GR_full_data_asym,1,0.4,0.4,0.16,0,0);

#save('/vega/ccls/users/cl3173/workspace/nlp/code/output/GR_Kernel_PT.mat','GR_PT_kernel','GR_PT_kernel_4');



