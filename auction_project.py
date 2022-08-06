bidder={} #declaring a dictionary
person=''
print(" lets begin the auction")
user_inp=input("do you want to apply for auction ")
user_inp1=user_inp
while(user_inp1=='yes'):
    
    name=input("enter your name ")
    money=int(input("what is amount that you want to bid "))
    bidder[name]=money
    user_inp1=input("do you want to apply for auction ")
    highest_money=0
for bidd,money in bidder.items():
       if(money>highest_money):
           highest_money=money
           person=bidd
print("the winner is "+person+" with money of "+str(highest_money))