# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 11:22:24 2023

@author: mikhal
"""
#תרגיל 1
def my_func(x1,x2,x3):
    if type(x1)== int and  type(x2)== int  and type(x3) == int:
        print("Error: parameters should be float")      
    elif type(x1)== float and  type(x2)== float  and type(x3) == float:
        if  x1+x2+x3==0:
            print ("Not a number – denominator equals zero")
        else:    
            print(float(((x1+x2+x3)*(x1+x2+x3))/(x1+x2+x3)))
    else:
        return None          


#targil 2
def revword(lowerword:str):
            lowerword = lowerword.lower()[::-1]
            return lowerword
def countword():        
    txt_ = open("text.txt", "r")
    for i in txt_:
        n=i.split()
        word=(n[0]).lower()
        break
    count = 1
    for i in txt_:
            lst=i.split()
            for j in lst:
                w1=revword(j)
                if w1 == word:
                    count+=1
                else:
                    continue
    print(count)
    
countword()
