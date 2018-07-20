# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:27:10 2018

@author: zhang_yu
"""
import re 

#初步分词
def splitmail(email):
    result=[]
    # 提取@之前的字符串
    premail=email.split('@')[0]
    #按数字切分字符串
    premaillist=re.split('\d+',premail)
    # 剔除空的字符串
    premaillist = [i for i in premaillist if len(i) > 0]
    for j in range(len(premaillist)):
        subemail=re.split('\\.|_',premaillist[j])
        subemail = [k for k in subemail if len(k) > 0]
        result=result+subemail
        return result
#n-gram分词
def extract(seq,kmin,kmax):
    result=[]
    if kmax>len(seq):
        kmax=len(seq)
    for j in range(kmin,kmax+1)[::-1]:
        length=len(seq)-j+1
        for i in range(length):
            result.append(seq[i:i+j])
    return result

#在分次之中检验结果：
def isfit(seq,kmin,kmax,lexicon,emailname,count):
    cnt=count
    result={}
    if kmin>len(seq):
        result[emailname,cnt]='No'
        cnt=cnt+1
        return result,cnt
    if kmax>len(seq):
        kmax=len(seq)
    flag=False
    for j in range(kmin,kmax+1)[::-1]:
        length=len(seq)-j+1
        for i in range(length):
            if str.lower(seq[i:i+j]) in lexicon:
                result[emailname,cnt]=seq[i:i+j]
                cnt=cnt+1
                flag=True
                break
        if flag==True:
            break
    if flag==False:
        result[emailname,cnt]='No'
    return (result,cnt)
    
#检验是否含有数字
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))
#检查是否含有特殊字符
def hasSpecialchar(inputString):
    return bool(re.search(r'&|@|!|%|\$|\^|\*|-$|\.',inputString))

#导入字典
def inputLexicon():
    lexicon=[]
    with open('lexicon.txt',encoding = 'ISO-8859-1') as f1:#打开'weibo_train_data.txt'文件
        for line in f1:  
            tmp=re.split('\t|\n',line)
            lexicon.append(str.lower(tmp[1]))
    lexicon=[k for k in lexicon if not hasSpecialchar(k)  and not hasNumbers(k)
        and k!='zzc' and len(k)>2 and k!='fo']  
    return lexicon
        



if __name__ == '__main__':
     #导入字典：
    lexicon=inputLexicon()
    #结果json文件,获取匹配结果
    result={}
    ## 读取邮箱
    #导入邮箱数据，并划分单词
    with open('maildata.txt') as  f1:#打开'weibo_train_data.txt'文件
        f11 = f1.read()#将打开文件的内容读到内存中，with 在执行完命令后，会关闭文件  
    listmail=f11.split('\n')
    for i in range(len(listmail)):
        spmail=splitmail(listmail[i])
        count=0
        for j in range(len(spmail)):
            tmpresult,count=isfit(spmail[j],4,10,lexicon,listmail[i],count)
            result={**result,**tmpresult}
    for email, fitValue in result.items():
        print(email,":",fitValue)
 
    
    
    # 提取@之前的字符串
#    a=listmail[i].split('@')[0]
#    # 按数字切分
#    a=re.split('\d+',a)
#    a = [i for i in a if len(i) > 0]
#    for j in range(len(a)):
#        b=re.split('\\.',a[j])
#        b = [i for i in b if len(i) > 0]
#        print(b)
#    

