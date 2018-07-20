# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:06:42 2018

@author: zhang_yu
"""

import re
def extract(seq,k):
    result=[]
    for j in range(k,len(seq)+1):
#        print(j)
        length=len(seq)-j+1
        for i in range(length):
#            print(i,"sds")
            result.append(seq[i:i+j])
    return result
#检验是否含有数字
def hasNumbers(inputString):
    return bool(re.search(r'\d', inputString))

def hasSpecialchar(inputString):
    return bool(re.search(r'&|@|!|%|\$|\^|\*|-$|\.',inputString))

#ISO-8859-1
result=[]
with open('lexicon.txt',encoding = 'ISO-8859-1') as f1:#打开'weibo_train_data.txt'文件
   for line in f1:  
       tmp=re.split('\t|\n',line)
       result.append(tmp[1])
#pattern=re.compile(r'\D+')
#result=[k for k in result if k[0:1]!='@' and k[0:1]!='-' and k[0:1]!='*' 
#        and k[0:1]!='&' and k[0:1]!='$'and k[0:1]!='^' and not hasNumbers(k)
#        and k!='zzc' and len(k)>2 and k!='fo'] 
result=[k for k in result if not hasSpecialchar(k)  and not hasNumbers(k)
        and k!='zzc' and len(k)>2 and k!='fo']        
#tmp=[k for k in tmp if len(k)>0]   

#for i in range(len(result)):
#    print(i,":",result[i])

fileObject = open('lexiconPro.txt', 'w')
for word in result:
	fileObject.write(word)
	fileObject.write('\n')
fileObject.close()
    



