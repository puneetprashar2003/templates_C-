import random
alpha_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars=['!','@','#','$','%','&','_']
num=['1','2','3','4','5','6','7','8','9','0']
pas=''
no_of_alpha=int(input("how many characters do you want in your pass word"))
no_of_specialchars=int(input("how many  special characters do you want in your pass word"))
numbers=int(input("how many numbers do you want in your password "))
ps_list=[]
for i in range(no_of_alpha):
    ps_list.append(random.choice(alpha_list))
for i in range(no_of_specialchars):
    ps_list.append(random.choice(special_chars))
for i in range(numbers):
    ps_list.append(random.choice(num))    
random.shuffle(ps_list)
for i in range(len(ps_list)):
    pas=pas+ps_list[i]
print(pas)                  

