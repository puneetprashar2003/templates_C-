import random
user=[]
sum1=0
sum2=0
computer=[]
sum_user=0
sum_computer=0
cards=['1','2',"3",'4','5','6','7','8','9','J','K','Q','A']
for i in range(2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))
print("your cards are "+user[0]+" " +user[1])
print("one of computers cards is "+computer[0])
for j in range(2):
        if(computer[j]=="J" or computer[j]=="K" or computer[j]=="Q" or computer[j]=="A" ):
            sum1=sum1+10
        else:
            sum1=sum1+int(computer[j])
for i in range(2):
        if(user[i]=="J" or user[i]=="K" or user[i]=="Q" or user[i]=="A" ):
            sum2=sum2+10
if((sum2)<17 ):
    choice='y'
else:

     choice=input("press y if you want to withdraw another card ")
if (choice=="y"):
    user.append(random.choice(cards))
    for i in range(3):
        if(user[i]=="J" or user[i]=="K" or user[i]=="Q" or user[i]=="A" ):
            sum_user=sum_user+10
        else:
            sum_user=sum_user+int(user[i])
    for j in range(2):
        if(computer[j]=="J" or computer[j]=="K" or computer[j]=="Q" or computer[j]=="A" ):
            sum_computer=sum_computer+10
        else:
            sum_computer=sum_computer+int(computer[j])
else:
    for j in range(2):
        if(computer[j]=="J" or computer[j]=="K" or computer[j]=="Q" or computer[j]=="A" ):
            sum_computer=sum_computer+10
        else:
            sum_computer=sum_computer+int(computer[j])
    for i in range(2):
        if(user[i]=="J" or user[i]=="K" or user[i]=="Q" or user[i]=="A" ):
            sum_user=sum_user+10
        else:
            sum_user=sum_user+int(user[i])
if((21-sum_user)<(21-sum_computer) and sum_user<=21):
    print("you won")
else:
    print("you lost")
print(user)
print(computer)


