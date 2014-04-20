#! /usr/bin/env python

import argparse
import xlwt
import re

parser = argparse.ArgumentParser(description="collect data from previous experimental")
parser.add_argument("-i","--input",dest="input_file",type=str)
parser.add_argument("-n","--nograph",dest="input_file2",type=str)
parser.add_argument("-o","--output",dest="output_file",type=str,default="output.xls")

options = parser.parse_args()

if not options.input_file:
    parser.error("you must specify a input file with -i or --input")

count = 0
with open(options.input_file,"r") as input_file:
    lines = input_file.readlines()

with open(options.input_file2,"r") as input_file2:
    lines2 = input_file2.readlines()


print lines[2][1:].replace("\n","").split(" ")

wb = xlwt.Workbook()

ws = wb.add_sheet('WithGraphKernel')
ws.write(0,0,"Index")
ws.write(0,1,"Kernel Structure Type")
ws.write(0,2,"Precision_Mean")
ws.write(0,3,"Precision_Std")
ws.write(0,4,"Recall_Mean")
ws.write(0,5,"Recall_Std")
ws.write(0,6,"FMeasure_Mean")
ws.write(0,7,"FMeasure_Std")
ws.write(0,8,"Best_C_Value")
for i in range(len(lines)/3):
    ws.write(i+1, 0, int(lines[3*i].replace("\n","")))
    ws.write(i+1, 1, lines[3*i+1])
    number_list = lines[3*i+2][1:].replace("\n","").split(" ")
    ws.write(i+1, 2, float(number_list[0]))
    ws.write(i+1, 3, float(number_list[1]))
    ws.write(i+1, 4, float(number_list[2]))
    ws.write(i+1, 5, float(number_list[3]))
    ws.write(i+1, 6, float(number_list[0]))
    ws.write(i+1, 7, float(number_list[1]))
    ws.write(i+1, 8, float(number_list[2]))

ws2 = wb.add_sheet('WithOutGraphKernel')
ws2.write(0,0,"Index")
ws2.write(0,1,"Kernel Structure Type")
ws2.write(0,2,"Precision_Mean")
ws2.write(0,3,"Precision_Std")
ws2.write(0,4,"Recall_Mean")
ws2.write(0,5,"Recall_Std")
ws2.write(0,6,"FMeasure_Mean")
ws2.write(0,7,"FMeasure_Std")
ws2.write(0,8,"Best_C_Value")
for i in range(len(lines2)/3):
    ws2.write(i+1, 0, int(lines2[3*i].replace("\n","")))
    ws2.write(i+1, 1, lines2[3*i+1])
    number_list = lines2[3*i+2][1:].replace("\n","").split(" ")
    ws2.write(i+1, 2, float(number_list[0]))
    ws2.write(i+1, 3, float(number_list[1]))
    ws2.write(i+1, 4, float(number_list[2]))
    ws2.write(i+1, 5, float(number_list[3]))
    ws2.write(i+1, 6, float(number_list[0]))
    ws2.write(i+1, 7, float(number_list[1]))
    ws2.write(i+1, 8, float(number_list[2]))


ws3 = wb.add_sheet('WithOutGraphKernelReal')
ws3.write(0,0,"Index")
ws3.write(0,1,"Kernel Structure Type")
ws3.write(0,2,"Precision_Mean")
ws3.write(0,3,"Precision_Std")
ws3.write(0,4,"Recall_Mean")
ws3.write(0,5,"Recall_Std")
ws3.write(0,6,"FMeasure_Mean")
ws3.write(0,7,"FMeasure_Std")
ws3.write(0,8,"Best_C_Value")
counter = 1
for i in range(len(lines2)/3):
    if re.match(r'.*(GRW|PST)_S2.*',lines2[3*i+1]) is None:
        ws3.write(counter, 0, int(lines2[3*i].replace("\n","")))
        ws3.write(counter, 1, lines2[3*i+1])
        number_list = lines2[3*i+2][1:].replace("\n","").split(" ")
        ws3.write(counter, 2, float(number_list[0]))
        ws3.write(counter, 3, float(number_list[1]))
        ws3.write(counter, 4, float(number_list[2]))
        ws3.write(counter, 5, float(number_list[3]))
        ws3.write(counter, 6, float(number_list[0]))
        ws3.write(counter, 7, float(number_list[1]))
        ws3.write(counter, 8, float(number_list[2]))
        counter+=1





ws4 = wb.add_sheet('BestKernelWithGraphKernel')

ws4.write(0,0,"GR")
ws4.write(0,1,"GR_PT_4")
ws4.write(1,0,"GRW")
ws4.write(1,1,"GRW_PT_4")
ws4.write(2,0,"PST")
ws4.write(2,1,"PST_SST_4")
ws4.write(3,0,"SEM1")
ws4.write(3,1,"SEM1_SP")
ws4.write(4,0,"SEM2")
ws4.write(4,1,"SEM2_SP")
ws4.write(5,0,"SEM3")
ws4.write(5,1,"SEM3_SP")
ws4.write(6,0,"GR_S2")
ws4.write(6,1,"GR_S2_PT_4")
ws4.write(7,0,"PST_S2")
ws4.write(7,1,"PST_S2_SP")
ws4.write(8,0,"SEM1_S2")
ws4.write(8,1,"SEM1_S2_SP") 
ws4.write(9,0,"SEM2_S2")
ws4.write(9,1,"SEM2_S2_SP")
ws4.write(10,0,"SEM3_S2")
ws4.write(10,1,"SEM3_S2_SP")
ws4.write(11,0,"GRW_S2")
ws4.write(11,1,"GRW_S2_SP")


ws5 = wb.add_sheet('BestKernelWithoutGraphKernel')

ws5.write(0,0,"GR")
ws5.write(0,1,"GR_PT_4")
ws5.write(1,0,"GRW")
ws5.write(1,1,"GRW_PT_4")
ws5.write(2,0,"PST")
ws5.write(2,1,"PST_SST_4")
ws5.write(3,0,"SEM1")
ws5.write(3,1,"SEM1_PT_4")
ws5.write(4,0,"SEM2")
ws5.write(4,1,"SEM2_PT_4")
ws5.write(5,0,"SEM3")
ws5.write(5,1,"SEM3_PT_4")
ws5.write(6,0,"GR_S2")
ws5.write(6,1,"GR_S2_PT_4")
ws5.write(7,0,"PST_S2")
ws5.write(7,1,"PST_S2_SP")
ws5.write(8,0,"SEM1_S2")
ws5.write(8,1,"SEM1_S2_PT_4") 
ws5.write(9,0,"SEM2_S2")
ws5.write(9,1,"SEM2_S2_PT_4")
ws5.write(10,0,"SEM3_S2")
ws5.write(10,1,"SEM3_S2_PT_4")
ws5.write(11,0,"GRW_S2")
ws5.write(11,1,"GRW_S2_SP")


wb.save(options.output_file)
