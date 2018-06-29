#coding:utf8
import os;
import json;

#排序
def sort(list):
    for i in range(len(list)):
        list[i] = list[i].split('.')
        list[i][0] = int(list[i][0])

    list.sort()

    for i in range(len(list)):
        list[i][0] = str(list[i][0])
        list[i] = list[i][0] + '.' + list[i][1]

    return list

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
    filelist = sort(filelist)
    namelist = getName()

    for files in filelist:#遍历所有文件
        
        Olddir = os.path.join(path,files);#原来的文件路径                
        if os.path.isdir(Olddir):#如果是文件夹则跳过
            continue;
        filename = os.path.splitext(files)[0];#文件名
        filetype = os.path.splitext(files)[1];#文件扩展名
        #Newdir=os.path.join(path,str(i)+filetype);#新的文件路径

        if str(i) == filename: #判断图片是否正确
            Newdir = os.path.join(path,namelist[i]+filetype);
            os.rename(Olddir,Newdir)#重命名

        i = i+1
rename()

#getName()

