import os
import random
from turtle import clear
dict_a={"pompu":1234,"tompu":11221,"gompu":1211}
dict_b={"alpha":111,"beta":999,"gamma":1212}

list1_key=[]
list1_items=[]
list2_key=[]
list2_items=[]
choice=1
while(choice==1):
    os.system('clear')
    randl=random.randint(0,2)
    rand2=random.randint(0,2)
    for key,values in dict_a.items():
        list1_key.append(key)
        list1_items.append(values)
    for key,values in dict_b.items():
        list2_key.append(key)
        list2_items.append(values)
    print("category A has "+ list1_key[randl])
    print ("category B has "+list2_key[rand2])
    choice_again=int(input("enter 1 if category A has  higher followers than B else enter 2 "))
    if(choice_again==1 and list1_items[randl]>list2_items[rand2]):
        print("thats right here you go")
    else:
        print ("you loose ")
        choice=0





