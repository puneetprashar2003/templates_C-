import random



rock='rock'
paper='paper'
scissor='scissor'
usser_comd=int(input("enter rock paper or scissor"))
computer_output=random.randint(0,2)
if(computer_output==0):
    print("it gave rock")
elif(computer_output==1):
    print("it gave paper")
elif(computer_output==2):
    print("it gave scissor")
if(computer_output==usser_comd):
    print("tie")
if(computer_output==0 and usser_comd==1):
    print("you won")   
if(computer_output==1 and usser_comd==0):
    print("you lost")   
if(computer_output==1 and usser_comd==2):
    print("you won")  
if(computer_output==2 and usser_comd==1):
    print("you lost")    
if(computer_output==0 and usser_comd==2):
    print("you lost") 
if(computer_output==0 and usser_comd==2):
    print("you won")