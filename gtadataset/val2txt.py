import os
import numpy as np
import time


gtrootdir=os.makedirs('evaluatedata/val',exist_ok=True)
rootpath='gtadataset/val_labels'
pathdir=os.listdir(rootpath)
print('clear old data')
for file_name in pathdir:
    write_path = os.path.join('evaluatedata/val/gtfolder',file_name)
    filewriter = open(write_path,'w')
print('start write gt txt')
for file_name in pathdir:
    #print(file_name)
    txt=[]
    bboxtext=[]
    read_path=os.path.join(rootpath,file_name)
    file_reader=open(read_path,'r')
    for line in file_reader.readlines():
        txt.append(line)
    #print(txt)
    for i in range(len(txt)):
        split_text=txt[i].split()
        xleft =int((float(split_text[1])-float(split_text[3])/2)*1920)
        ytop=int((float(split_text[2])-float(split_text[4])/2)*1080)
        xright=int((float(split_text[1])+float(split_text[3])/2)*1920)
        ybuttom=int((float(split_text[2])+float(split_text[4])/2)*1080)
        bboxtext.append([xleft,ytop,xright,ybuttom])
    #print(bboxtext)
    write_path = os.path.join('evaluatedata/val/gtfolder',file_name)
    filewriter = open(write_path,'a')
    for i in range(len(bboxtext)):
        filewriter.write('0 ')
        filewriter.write(str(bboxtext[i][0])+' '+str(bboxtext[i][1])+' '+str(bboxtext[i][2])+' '+str(bboxtext[i][3]))
        filewriter.write('\n')
print('writting done!')
