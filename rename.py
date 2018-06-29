#coding:utf8
import os;
import json;

#读取json中的数据
def getName(): 
    path = "C:\\Users\\Administrator\\Desktop\\name.json";
    with open(path,'r') as f:
        temp = json.loads(f.read())
    return temp['name']

def rename():
    i = 0
    path = "C:\\Users\\Administrator\\Desktop\\photo";
    filelist = os.listdir(path)#该文件夹下所有的文件（包括文件夹）
    namelist = getName()
    
    for files in filelist:#遍历所有文件
        
        Olddir = os.path.join(path,files);#原来的文件路径                
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue;
        filename = os.path.splitext(files)[0];#文件名
        filetype = os.path.splitext(files)[1];#文件扩展名
        #Newdir=os.path.join(path,str(i)+filetype);#新的文件路径
        Newdir = os.path.join(path,namelist[i]+filetype);

        os.rename(Olddir,Newdir)#重命名
        i = i+1
rename()

#getName()
