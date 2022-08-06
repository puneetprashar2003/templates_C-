choice=int(input("enter 1 to encode and 2 to decode"))
word=input("enter the word")
str=''
number_jump=int(input('enter the number to jump'))
for i in range(len(word)):
    if(choice==1):

        final_word_integer=ord(word[i])+number_jump
    elif(choice==2):
        final_word_integer=ord(word[i])-number_jump
    str=str+chr((final_word_integer)%122)

print(str)