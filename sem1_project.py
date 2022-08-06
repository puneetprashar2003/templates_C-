import random 
import os
word_list=(["absence","abuse","account","accident","beneath","bend","benefit","biology","bitter","candidate","campaign","camera","capacity","capture","deaf","daughter","deal","decorate","dialogue","economy","finance","educate","efficient","supportive","elderly","flight","folk","flame","frustration","garbage","gather","gentle","global","hilarious","intelligence","jazz","knife","longevity","momument","nonsense","nobody","turmeric","utilize","sashimi","reconfigure","wheat","yellowish","zone"])
print("you have 7 lives")
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
end_of_game=False
lives=7
disp=[]
for _ in range(word_length):
    disp+="_"
print("the word has "+str(word_length)+" alphabets")

while not end_of_game:
    guess=input("enter an alphabet ").lower()
    if guess in disp:
        print(f"you have already guessed {guess}")
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            disp[position]=letter
    if guess not in chosen_word:
        lives-=1
        
        print("number of lives left "+str(lives))
            
        if(lives==0):
            print("you loose")
            break
    print(f"{''.join(disp)}")
    if "_" not in disp:
        end_of_game=True
        print("you won")
        