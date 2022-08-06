num1=int(input("enter a number"))

choice="y"
while(choice=='y'):
    operand=input("enter an operand")
    num2=int(input("enter another number "))
    if(operand=="+"):
        print(str(num1 )+ operand+ str(num2)+"="+ str(num1+num2))
        num1=num1+num2
    if(operand=="-"):
        print(str(num1 )+ operand+ str(num2)+"="+ str(num1-num2))
        num1=num1-num2
    if(operand=="*"):
        print(str(num1 )+ operand+ str(num2)+"="+ str(num1*num2))
        num1=num1*num2
    if(operand=="/"):
        print(str(num1 )+ operand+ str(num2)+"="+ str(num1/num2))
        num1=num1/num2
    choice=input("press y if you want to continue the game ")