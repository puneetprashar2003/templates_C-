for i in range(0,101):
    if(i%15==0):
        print("fizzbuzz")
    elif(i%3==0 and not(i%5==0)):
        print("fizz")
    elif(i%5==0 and not(i%3==0)):  
        print("buzz")
    else:
        print(i)          
