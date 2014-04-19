#! /bin/env python2.7
'''
this python script receive the kernel type and make the combination of the kernels according to the parameter 
'''
import os
import argparse
import sys
import shutil



dir_prefix=''
data_dir_prefix='../../folds_data'
tag_dir_prefix='../../tags'

original_dir = "../original"
combination_dir = "../combination"
template_dir = "../templates"
libsvm_path = '../../libsvm'

kernel_dict={}
folds=0


c_values = "-3:0.02:5"
#[int(a[i:i+1]) for i in range(0, len(a), 1)]



#GR = {"PT":"GR_PT_4","SST":"GR_SST_4","WL":"GR_WL","SP":"GR_SP"}
#GRW = {"PT":"GRW_PT_4","SST":"GRW_SST_4","WL":"GRW_WL","SP":"GRW_SP"}
#PST = {"PT":"PST_PT_4","SST":"PST_SST_4","WL":"PST_WL","SP":"PST_SP"}
#SEM1 = {"PT":"SEM1_PT_4","SST":"SEM1_SST_4","WL":"SEM1_WL","SP":"SEM1_SP"}
#SEM2 = {"PT":"SEM2_PT_4","SST":"SEM2_SST_4","WL":"SEM2_WL","SP":"SEM2_SP"}
#SEM3 = {"PT":"SEM3_PT_4","SST":"SEM3_SST_4","WL":"SEM3_WL","SP":"SEM3_SP"}

GR = ["GR_PT_4","GR_SST_4"]
GRW = ["GRW_PT_4","GRW_SST_4"]
PST = ["PST_PT_4","PST_SST_4"]
SEM1 = ["SEM1_PT_4","SEM1_SST_4"]
SEM2 = ["SEM2_PT_4","SEM2_SST_4"]
SEM3 = ["SEM3_PT_4","SEM3_SST_4"]

original_struct_list = [GR,GRW,PST,SEM1,SEM2,SEM3]

#GR_S2 = {"PT":"GR_S2_PT_4","SST":"GR_S2_SST_4","WL":"GR_S2_WL","SP":"GR_S2_SP"}
#GRW_S2 = {"PT":"GRW_S2_PT_4","SST":"GRW_S2_SST_4","WL":"GRW_S2_WL","SP":"GRW_S2_SP"}
#PST_S2 = {"PT":"PST_S2_PT_4","SST":"PST_S2_SST_4","WL":"PST_S2_WL","SP":"PST_S2_SP"}
#SEM1_S2 = {"PT":"SEM1_S2_PT_4","SST":"SEM1_S2_SST_4","WL":"SEM1_S2_WL","SP":"SEM1_S2_SP"}
#SEM2_S2 = {"PT":"SEM2_S2_PT_4","SST":"SEM2_S2_SST_4","WL":"SEM2_S2_WL","SP":"SEM2_S2_SP"}
#SEM3_S2 = {"PT":"SEM3_S2_PT_4","SST":"SEM3_S2_SST_4","WL":"SEM3_S2_WL","SP":"SEM3_S2_SP"}

GR_S2 = ["GR_S2_PT_4","GR_S2_SST_4"]
GRW_S2 = ["GRW_S2_PT_4","GRW_S2_SST_4"]
PST_S2 = ["PST_S2_PT_4","PST_S2_SST_4"]
SEM1_S2 = ["SEM1_S2_PT_4","SEM1_S2_SST_4"]
SEM2_S2 = ["SEM2_S2_PT_4","SEM2_S2_SST_4"]
SEM3_S2 = ["SEM3_S2_PT_4","SEM3_S2_SST_4"]

struct_file_data_dict = {}

struct_file_data_dict["GR"] = ["GR_PT_4","GR_SST_4"]
struct_file_data_dict["GRW"] = ["GRW_PT_4","GRW_SST_4"]
struct_file_data_dict["PST"] = ["PST_PT_4","PST_SST_4"]
struct_file_data_dict["SEM1"] = ["SEM1_PT_4","SEM1_SST_4"]
struct_file_data_dict["SEM2"] = ["SEM2_PT_4","SEM2_SST_4"]
struct_file_data_dict["SEM3"] = ["SEM3_PT_4","SEM3_SST_4"]
struct_file_data_dict["GR_S2"] = ["GR_S2_PT_4","GR_S2_SST_4"]
struct_file_data_dict["GRW_S2"] = ["GRW_S2_PT_4","GRW_S2_SST_4"]
struct_file_data_dict["PST_S2"] = ["PST_S2_PT_4","PST_S2_SST_4"]
struct_file_data_dict["SEM1_S2"] = ["SEM1_S2_PT_4","SEM1_S2_SST_4"]
struct_file_data_dict["SEM2_S2"] = ["SEM2_S2_PT_4","SEM2_S2_SST_4"]
struct_file_data_dict["SEM3_S2"] = ["SEM3_S2_PT_4","SEM3_S2_SST_4"]



kernel_list=["PT","SST","WL","SP"]
kernel_dict["GR"] = {"PT":"GR_PT_4","SST":"GR_SST_4","WL":"GR_WL","SP":"GR_SP"}
kernel_dict["GRW"] = {"PT":"GRW_PT_4","SST":"GRW_SST_4","WL":"GRW_WL","SP":"GRW_SP"}
kernel_dict["PST"] = {"PT":"PST_PT_4","SST":"PST_SST_4","WL":"PST_WL","SP":"PST_SP"}
kernel_dict["SEM1"] = {"PT":"SEM1_PT_4","SST":"SEM1_SST_4","WL":"SEM1_WL","SP":"SEM1_SP"}
kernel_dict["SEM2"] = {"PT":"SEM2_PT_4","SST":"SEM2_SST_4","WL":"SEM2_WL","SP":"SEM2_SP"}
kernel_dict["SEM3"] = {"PT":"SEM3_PT_4","SST":"SEM3_SST_4","WL":"SEM3_WL","SP":"SEM3_SP"}
kernel_dict["GR_S2"] = {"PT":"GR_S2_PT_4","SST":"GR_S2_SST_4","WL":"GR_S2_WL","SP":"GR_S2_SP"}
kernel_dict["GRW_S2"] = {"PT":"GRW_S2_PT_4","SST":"GRW_S2_SST_4","WL":"GRW_S2_WL","SP":"GRW_S2_SP"}
kernel_dict["PST_S2"] = {"PT":"PST_S2_PT_4","SST":"PST_S2_SST_4","WL":"PST_S2_WL","SP":"PST_S2_SP"}
kernel_dict["SEM1_S2"] = {"PT":"SEM1_S2_PT_4","SST":"SEM1_S2_SST_4","WL":"SEM1_S2_WL","SP":"SEM1_S2_SP"}
kernel_dict["SEM2_S2"] = {"PT":"SEM2_S2_PT_4","SST":"SEM2_S2_SST_4","WL":"SEM2_S2_WL","SP":"SEM2_S2_SP"}
kernel_dict["SEM3_S2"] = {"PT":"SEM3_S2_PT_4","SST":"SEM3_S2_SST_4","WL":"SEM3_S2_WL","SP":"SEM3_S2_SP"}



best_kernel_dict={}

best_kernel_dict["GR"] = "GR_PT_4"
best_kernel_dict["GRW"] = "GRW_PT_4"
best_kernel_dict["PST"] = "PST_SST_4"
best_kernel_dict["SEM1"] = "SEM1_PT_4"
best_kernel_dict["SEM2"] = "SEM2_SP"
best_kernel_dict["SEM3"] = "SEM3_SP"
best_kernel_dict["GR_S2"] = "GR_S2_PT_4"
best_kernel_dict["PST_S2"] = "PST_S2_SST_4"
best_kernel_dict["SEM1_S2"] = "SEM1_S2_SP" 
best_kernel_dict["SEM2_S2"] = "SEM2_S2_SP"
best_kernel_dict["SEM3_S2"] = "SEM3_S2_SP"
best_kernel_dict["GRW_S2"] = "GRW_S2_SP"


struct_dir_dict={}

struct_dir_dict["GR"] = "GR"
struct_dir_dict["GRW"] = "GRW"
struct_dir_dict["PST"] = "PST"
struct_dir_dict["SEM1"] = "SEM1"
struct_dir_dict["SEM2"] = "SEM2"
struct_dir_dict["SEM3"] = "SEM3"
struct_dir_dict["GR_S2"] = "GR"
struct_dir_dict["PST_S2"] = "PST"
struct_dir_dict["SEM1_S2"] = "SEM1" 
struct_dir_dict["SEM2_S2"] = "SEM2"
struct_dir_dict["SEM3_S2"] = "SEM3"
struct_dir_dict["GRW_S2"] = "GRW"


s2_struct_list = [GR_S2,GRW_S2,PST_S2,SEM1_S2,SEM2_S2,SEM3_S2]

all_struct_list = [GR,GRW,PST,SEM1,SEM2,SEM3,GR_S2,GRW_S2,PST_S2,SEM1_S2,SEM2_S2,SEM3_S2]

all_struct_name = ["GR","GRW","PST","SEM1","SEM2","SEM3","GR_S2","GRW_S2","PST_S2","SEM1_S2","SEM2_S2","SEM3_S2"]


template="""#PBS -W group_list=yeticcls
#PBS -l nodes=1,walltime=10:00:00,mem=8gb
#PBS -M cl3173@columbia.edu 
#PBS -m abe 
#PBS -V 
# Set output and error directories 
#PBS -o localhost:/vega/ccls/users/cl3173/ 
#PBS -e localhost:/vega/ccls/users/cl3173/ \n"""
 

def main():
    global libsvm_path
    global dir_prefix
    parser = argparse.ArgumentParser(description="yeti generating test set script")
    # 0 means original 1 means combination
    parser.add_argument('-t',"--type",dest='type',type=int,choices=[0,1])
    parser.add_argument('-d',"--debug",dest='debug',type=int,choices=[0,1],default=0)
    parser.add_argument('-f',"--folds",dest='folds',type=int,default=0)
    options = parser.parse_args()

    if options.folds<=0:
        print "you must specify the folds number by -f or --folds"
        sys.exit(1)

    folds = options.folds
    if options.debug:
        print original_struct_list
        print s2_struct_list

    if options.type is None:
        print "type option is needed"
        sys.exit(1)

    libsvm_path = libsvm_path + '/matlab'
    
    if not options.type:
        dir_prefix = original_dir

        if not os.path.exists(dir_prefix):
            os.mkdir(dir_prefix)

        for struct in all_struct_name:
            if not os.path.exists(dir_prefix+"/"+struct):
                os.mkdir(dir_prefix+"/"+struct)
            with open(dir_prefix+"/"+struct+'/output','w') as record_output:
                record_output.write(struct+'\n')

            genBash(struct)
            shutil.copyfile(template_dir+'/svm_test.m',dir_prefix+"/"+struct+'/svm_test.m')
            run_m = open(dir_prefix+"/"+struct+'/batch_run.m','w')
            for fold in range(folds):
                run_m.write("load(\'%s.mat\');\n"%(tag_dir_prefix+"/"+str(fold)))
                for file_name in struct_file_data_dict[struct]:
                    run_m.write("load(\'%s.mat\');\n"%(data_dir_prefix+"/fold_"+str(fold)+"/"+struct_dir_dict[struct]+"/full/"+file_name+"_fold_"+str(fold)))

            run_m.write("c_values = %s;\n"%(c_values))
            run_m.write("fid = fopen(\'output\',\'a+\');")

            for kernel in kernel_list:
                run_m.write("%s_precision_full=[];\n"%(kernel_dict[struct][kernel]))
                run_m.write("%s_recall_full=[];\n"%(kernel_dict[struct][kernel]))
                run_m.write("%s_f_measure_full=[];\n"%(kernel_dict[struct][kernel]))
                for  fold in range(folds):
                    run_m.write("%s_result_full_fold_%s=svm_test(%s,%s,%s,c_values);\n"%(kernel_dict[struct][kernel],str(fold),kernel_dict[struct][kernel]+"_fold_"+str(fold),str("tag_fold_"+str(fold)),str("sep_fold_"+str(fold))))
                    run_m.write("%s_precision_full=[%s_precision_full,%s_result_full_fold_%s(:,1)];\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],str(fold)))
                    run_m.write("%s_recall_full=[%s_recall_full,%s_result_full_fold_%s(:,2)];\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],str(fold)))
                    run_m.write("%s_f_measure_full=[%s_f_measure_full,%s_result_full_fold_%s(:,3)];\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],str(fold)))
                run_m.write("%s_mean_precision=mean(%s_precision_full,2);\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_mean_recall=mean(%s_recall_full,2);\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_mean_f_measure=mean(%s_f_measure_full,2);\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))

                run_m.write("%s_std_precision=std(%s_precision_full\')\';\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_std_recall=std(%s_recall_full\')\';\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_std_f_measure=std(%s_f_measure_full\')\';\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_result_full=[%s_mean_precision,%s_std_precision,%s_mean_recall,%s_std_recall,%s_mean_f_measure,%s_std_f_measure,10.^c_values\'];\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_result_full=sortrows(%s_result_full,5);\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))
                run_m.write("%s_result=%s_result_full(end,:);\n"%(kernel_dict[struct][kernel],kernel_dict[struct][kernel]))

                run_m.write("fprintf(fid,\'%s: %%0.6f %%0.6f %%0.6f %%0.6f %%0.6f %%0.6f %%0.6f \\n\',%s_result.\');\n"%(kernel,kernel_dict[struct][kernel]))

#            for line in run_template:
#                if line=="need_to_be_replace_pt\n":
#                    run_m.write("pt_result_full=svm_test(%s,struct_tag_full,%s)\n"%(struct_dict[struct]["PT"],str(sep)))
#                elif line=="need_to_be_replace_sst\n":
#                    run_m.write("sst_result_full=svm_test(%s,struct_tag_full,%s)\n"%(struct_dict[struct]["SST"],str(sep)))
#                elif line=="need_to_be_replace_wl\n":
#                    run_m.write("wl_result_full=svm_test(%s,struct_tag_full,%s)\n"%(struct_dict[struct]["WL"],str(sep)))
#                elif line=="need_to_be_replace_sp\n":
#                    run_m.write("sp_result_full=svm_test(%s,struct_tag_full,%s)\n"%(struct_dict[struct]["SP"],str(sep)))
#                else:
#                    run_m.write(line)
            run_m.write("save(\'./result.mat\');\n")
            run_m.write("fclose(fid);\n")
            run_m.close()
    else:
        dir_prefix = combination_dir
        genCombination(options.debug)


#    global full_path
#    full_path = os.getcwd()
#    directory_list=os.listdir(dir_prefix)
#
#    for ins in directory_list:
#        #print ins
#        if os.path.exists(dir_prefix+'/'+ins+'/run.sh'):
#            #print str(ins) + " has the bash script and we delete it"
#            try:
#                os.remove(dir_prefix+'/'+ins+'/run.sh')
#            except Exception,e:
#                print e
#                pass
#        genBash(ins)

def genOrignal():
    pass

def genCombination(debug):
    size = len(all_kernel_name)
    total_size = 2**size
    print size
    print total_size
    if not os.path.exists(full_path+'/'+combination_dir):
        os.mkdir(full_path+'/'+combination_dir)
    if debug:
        total_size = int(total_size*0.02)
    for i in range(total_size):
        if i != 0:
            if len(str(bin(i))[2:]) < 12:

                cur_string = "0"*(12-len(str(bin(i))[2:]))+str(bin(i))[2:]
            else:
                cur_string =  str(bin(i)[2:])
            cur = [int(cur_string[i:i+1]) for i in range(0, len(cur_string), 1)]
            weight = sum(cur)
            cur = zip(range(size),cur)
            #print cur
            weight_string = '*(1/%s)'%(weight)
            new_kernel = ''
            combination_name = ''
            for ele in cur:
                if ele[1]:
                    if new_kernel:
                        #new_kernel = new_kernel + '+' +kernel_dict[all_kernel_name[ele[0]]]['PT']+weight_string
                        new_kernel = new_kernel + '+' +best_kernel_dict[all_kernel_name[ele[0]]]+weight_string
                        combination_name = combination_name + '_' + all_kernel_name[ele[0]]
                    else:
                        new_kernel = best_kernel_dict[all_kernel_name[ele[0]]]+weight_string
                        combination_name = all_kernel_name[ele[0]]
            #print combination_name
            new_kernel = 'new_kernel=' + new_kernel +";\n"
            #print new_kernel
            if not os.path.exists(full_path+'/'+combination_dir+'/'+combination_name):
                os.mkdir(full_path+'/'+combination_dir+'/'+combination_name)
            with open(full_path+'/'+combination_dir+'/'+combination_name+'/output','w') as record_output:
                record_output.write(combination_name+'\n')
            genBash(combination_name)
            shutil.copyfile(full_path+'/'+template_dir+'/svm_test.m',full_path+'/'+combination_dir+'/'+combination_name+'/svm_test.m')
            run_m = open(full_path+'/'+combination_dir+'/'+combination_name+'/batch_run.m','w')
            run_m.write("load(\'%s/all_kernel.mat\')\n"%(full_path))
            run_m.write("addpath(\'%s\')\n"%(libsvm_path))
            run_m.write(new_kernel)
            run_m.write("result_full=svm_test(new_kernel,struct_tag_full,%s);\n"%(str(sep)))
            run_template = open(full_path+'/'+template_dir+'/com.m','r')
            for line in run_template:
                run_m.write(line)
            run_template.close()
            run_m.close()
    pass

def genBash(ins):
    with open('./'+dir_prefix+'/'+ins+'/run.sh','w') as bash_file:
        bash_file.write("#! /bin/sh\n#directives\n#PBS -N EXP_BEST_KERNEL_%s\n"%(ins))
        bash_file.write(template)
        #bash_file.write("cd "+full_path+'/'+dir_prefix+"/%s\n\n"%(ins))
        #remember EOL
        bash_file.write("matlab -nojvm -nodisplay -nosplash -r \"run(\'batch_run.m\');quit\" > EXP_BEST_KERNEL_%s\n"%(ins))

if __name__ == "__main__":
    main()





