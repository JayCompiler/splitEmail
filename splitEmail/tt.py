# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 10:41:00 2018

@author: zhang_yu
"""
import re
#pattern=re.compile(r'\D+|@|^')
 
def hasNumbers(inputString):
    return bool(re.search(r'\D|@|^', inputString))
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None

#a=bool(re.search(r'\d|@|\^|&|!|%|\$', 'ghsdhj'))
#print(a)

for i in range(2,10)[::-1]:
    print(i)

result={}
a=['asdc','cds','cdsa']
if 'cds' in a:
   result['cds']=True
if 'cds' in a:
   result['cds']=False
b={'sda':True}
c={**b,**result}
for key, value in c.items():
    print( key, ':',  value)
    

print(str.lower('SAD'))
a=[1,2,3;23,5,6,7;7,7,9]
print(a)
    
#print(hasNumbers('2313'))
#
#print(True or False)
 
#if match:
#    # 使用Match获得分组信息
#    print match.group()