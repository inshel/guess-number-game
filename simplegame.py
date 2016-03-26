import random
print("guess a number between 1 and 100")
correctNumber=random.randint(1,100)
guess=int(input("have a guess:"))
triesList=[guess]

while guess!=correctNumber:
     if guess<correctNumber:
        print("too low")
        guess=int(input("have a guess:"))
        if guess not in triesList:
           triesList.append(guess)
        else:
           print("you have previously guessed this number,pleas try again")
           guess=int(input("have a guess:"))
     else:
        print("too high")
        guess=int(input("have a guess:"))
        if guess not in triesList:
           triesList.append(guess)
        else:
           print("you have previously guessed this number,pleas try again")
           guess=int(input("have a guess:"))

print("Congratulations! the number is:",correctNumber,"and you have tried ",len(triesList),"times")





