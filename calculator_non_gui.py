s=0
def add(num1,num2):
    return(num1+num2)
def subtract(num1,num2):
    return(num1-num2)
def multi(num1,num2):
    return(num1*num2)
def divide(num1,num2):
    return(num1/num2)
choice="yes"

while(choice=="yes"):
    inp_1=int(input("enter _the first number"))
    inp_2=int(input("enter the second number"))
    operand=input("enter the operand")
    if(operand=="+"):

        s=s+add(inp_1,inp_2) 
    if(operand=="-"):
        s=s-subtract(inp_1,inp_2)
    if(operand=="*"):
        if(s==0):
            s=1*multi(inp_1,inp_2)
        else:
            s=s*multi(inp_1,inp_2)
    if(operand=="/"):
        s=s+divide(inp_1,inp_2)           
    choice1=input("do you want to continue")
    choice=choice1
print(s)