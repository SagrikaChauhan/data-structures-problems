# -*- coding: utf-8 -*-
"""
Created on Sat May 18 06:29:44 2019

@author: Sagrika
"""
def maxProduct(arr, n): 
  
    if (n < 2): 
        print("No pairs exists") 
        return
   
    result=0
    for i in range(0, n): 
          
        for j in range(i + 1, n): 
            if (arr[i] * arr[j] > result): 
                result = arr[i] * arr[j]
  
    print(result)
    
n = int(input())     

arr = list(map(int,input().rstrip().split()))


maxProduct(arr, n)