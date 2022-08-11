import random                               #importing the 'random' package for the generation of a random number
from colorama import Fore, init, Back, Style  # importing the 'colorama' package for giving a colored output
ans =[]
with open("ANSWERS.txt" , "r") as a_Read:       #Reading file 'ANSWERS.txt' and closing it once used
    for x in a_Read:
        ans.append(x.strip())                   #Making a list of the possible answers to choose on by the program
answer = ans[random.randint(0 , 2315)]      #Choosing a random word to be held as the answer for a single execution of the program
ans_List = []
for i in range(0, 5):
    ans_List.append(answer[i])              #Storing the letters of the 'answer' word individually
guess_List = []
count = 0
chance = 6                                  #Alloting 6 chances for the player
with open("ANSWERS.txt" , "r") as g_Read:            #Reading file 'GUESS.txt' and closing it once used
    for x in g_Read:
        guess_List.append(x.strip())            #Making a list of the possible guess words to check on once the user puts his word
alph_Used =[]
with open("INSTRUCTIONS.txt", "r") as dis:
    print(dis.read())


def guess_check(b):                             #Creating a functon block to check the guess word with the possible answer
    init(autoreset=True)                        #Resets the color of the output text once applied
    if b in guess_List:                         #Checking whether the input word is in the guess list
        global count                            # Used as a condition when whether all five letters are at correct place
        for j in range(0, 5):
            guess_slice.append(b[j])            #separating and storing of the guess word's letters
        count = 0                               # Declaring base value as zero
        for j in range(0, 5):
            if guess_slice[j].upper() not in alph_Used:    #Used letters are stored in a list
                alph_Used.append(guess_slice[j].upper())
            if guess_slice[j] in ans_List:                 #If the letter is present in answer word
                if guess_slice[j] in ans_List[j]:
                    count += 1
                    print(Fore.LIGHTGREEN_EX + f"{guess_slice[j].upper()} " + Back.BLACK + Style.BRIGHT ,end =" ")  # To print the 'green' condition
                else:
                    print(Fore.LIGHTYELLOW_EX + f"{guess_slice[j].upper()} " + Back.BLACK + Style.BRIGHT ,end =" ")  # To print the 'yellow' condition
            else:
                print(Fore.LIGHTWHITE_EX + f"{guess_slice[j].upper()} " + Back.BLACK + Style.BRIGHT ,end =" ")        # To print the 'white' condition
    else:
        print(" Please write a meaningful word which has a dictionary value on the OXFORD DICTIONARY Version 12.4. 191 (2020)") #If guess is not a meaningful word


while chance > 0:  #Condition to check player has six chances
    guess_slice = []
    a = input("\nEnter the guessing word: ")
    if not a.isalpha():
        print("BUZZZZZ    ERROR YOU CAN'T PUT NUMBERS OR SYMBOLS BUZZZZZZZZZZZ KINDY DON'T REPEAT")   #Rejecting symbols or numbers
        continue
    elif len(a)!= 5:
        print(f"THE WORD {a} IS NOT A 5 LETTER WORD............KINDLY PUT 5 LETTER WORDS ONLY ")  #Rejecting non five letter words
        continue
    else:
        guess_check(a.lower())    #Calling the function guess_list
        print("\nAlphabets used up: " , end ="")
        print(alph_Used)
        chance -= 1
        if count == 5:
            print(f"CONGRATS ON GUESSING THE WORD {a.upper()} WHICH WAS ANSWER!!!!!!!!  ON YOUR TRY NO: {6 - chance} ")  #Congratulating user on guessing the correct answer
            break

if count != 5 :
    print(f"   OOOOPPPSSSS  THE GUESS WORDS UNTIL NOW WERE NOT THE ANSWER!!!!!!!! INSTEAD THE WORD WAS (''' {answer.upper()} ''') ...... hey!!! IT DOES'NT MATTER BECOZ LIFE GIVES YOU CHANCES ANYTIME.... AND MORE IMPORTANTLY TEACHES US TO TAKE CALCULATED RISKS")  #Telling user that he lost the game

