import random
word_list=["apple","mango","grapes","pomegranate"]
print("you have 7 lives")
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
end_of_game=False
lives=7
display=[]
for _ in range(word_length):
    display+="_"
print("the word has "+str(word_length)+" alphabets")

while not end_of_game:
    guess=input("enter an alphabet").lower()
    if guess in display:
        print(f"you have already guessed {guess}")
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            display[position]=letter
    if guess not in chosen_word:
        lives-=1
        print("number of lives left"+str(lives))
        if(lives==0):
            print("you loose")
    print(f"{''.join(display)}")
    if "_" not in display:
        end_of_game=True
        print("you won")