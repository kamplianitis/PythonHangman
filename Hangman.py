import random

def printStart():
    print("Welcome to Hangman!")
    print("For new game press (1)")
    print("For exiting the game press 2")

def loadword():
    lines =open('sowpods.txt').read().splitlines()
    word = random.choice(lines)
    print(word)
    return word # return the value so that i can use it later

def hangword(word):
    hiddenword = []
    for i in range(len(word)): # add unknown segments .. must be the game ammount as the ammount of letters
        hiddenword.append("_")
    return hiddenword

def wincondition(hidden, word): # check if the word as it is now is same with the game-win word
    strtemp=""
    str = strtemp.join(hidden)
    if str == word:
        end = 1
    else:
        end = 0
    return end



# function that updates


def findword(word, hidden):
    end =0
    timesofplaying = 6
    incorectletters= []

    while timesofplaying >0 and end ==0:
        print(*hidden)
        pos = 0
        print("You have ", timesofplaying, "more tries")
        letter = input("Guess a letter: ")
        if 0<len(letter) <2:
            if hidden.count(letter) == 0 and incorectletters.count(letter) == 0:
                if word.count(letter) == 0:
                    print("Incorrect!")
                    incorectletters.append(letter)
                    print("Icorrect letters: ", incorectletters)
                    timesofplaying = timesofplaying -1
                else:
                    for x in range(word.count(letter)):
                        pos = word.find(letter, pos+x)
                        hidden[pos] = letter
                    end = wincondition(hidden, word)
            else:
                print("You have already written this  letter")
        else:
            print("ERROR: You need to put only one character")
    if timesofplaying == 0:
        print("Sorry but you lost.")
        print("The word was: ", word, "\n")
    elif end==1:
        print("Congratulations you have won the game. \n")



while 1:
    printStart()
    choice = input("Please give your choice: ")
    try:
        choice = int(choice)
        if choice == 1:
            print("\npreparing the new game")
            word = loadword() #the word chosen randomly 
            #comment the 2 lines below so you can play the game. There are in here for test purposes
            #print("The chosen word is: ",word)
            #hidden = hangword(word)
            print("Hidden word: ", *hidden)
            print(len(hidden))
            findword(word,hidden)
        elif choice ==2:
            print("Thank you for playing! \n")
            break
        else:
            print("Please give a value between 1 and 2\n")
    except:
        print("ERROR: Please give an Integer between 1 and 2\n")
