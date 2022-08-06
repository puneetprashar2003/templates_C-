import os
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk":0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


os.system('clear')
ready=1
while(ready==1):
    print("what will you like to have ?(espresso/latte/cappuccino)")
    choice=input("")
    if(choice=="report"):
        for key,values in resources.items():
            print(key+" "+str(values))
        print("what will you like to have ?(espresso/latte/cappuccino)")
        choice=input("")
    for key,values in MENU.items():
        if(choice==key):
            data_of_coffee=values
    for keys,values in data_of_coffee.items():
        if(keys=="ingredients"):
            data_of_coffee_ingredients=values
        else:
            data_of_coffee_cost=values
    for keys,values in data_of_coffee_ingredients.items():
        for keys1,values1 in resources.items():
            if(keys==keys1 and values>values1):
                ready=ready-1
    if(ready==1):
        print("the cost of " + choice+" is " +str(data_of_coffee_cost)+"$")
        quarters=int(input("how many quarters?"))
        dimes =int(input("how many dimes?"))
        pennies=int(input("how many pennies?"))
        nickles=int(input("how many nickles?"))
        total=0.25*quarters +0.1*dimes +0.01*pennies +0.05*nickles
        if(total>=data_of_coffee_cost):
            print("this is your change $"+str(total-data_of_coffee_cost))
            print("enjoy your coffee")
            for items in resources:
                resources[items]=resources[items]-data_of_coffee_ingredients[items]
                

        else:
            print("insufficient money")
        
    else:
        print("sorry we have insufficient material")
    