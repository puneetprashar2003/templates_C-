from cmath import pi
import math
tests=int(input())
list1=[]

for i in range(tests):
     sum=0
     list1=list(map(int,input().split()))
     r=list1[0]
     a1=r
     a=list1[1]
     b=list1[2]
     while(r!=0):
         sum=sum+pi*(r*a)**2
         r=r*a
         
         sum=sum+pi*(r//b)**2
         r=r//b         
     print("Case #"+str(i+1)+":  "+str(sum+pi*a1*a1))
         