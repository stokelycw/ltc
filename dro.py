#   Dice Rolling Simulator
#   Guess the absolute value of the  two rolls

from random import randint
def diceroller():
#   Die 1: take user's guess, then choose 
    print("Let's roll the dice. Can you guess the numbers between 1 and 6?")
    x = int(input("Die #1: "))
    a = (randint(1,6))

#   Die 2: take user's guess, then choose
    w = int(input("Die #2: "))
    b = (randint(1,6))

#   Total the guesses and the rolled numbers.
    z = (x+w)
    c = (a+b)

#   Show the results
    print("Fate chose "+str(a)+" and "+str(b))
    if abs(z-c)==0:
        print("How did you do that?!")
    if abs(z-c)!=0:
        print("You were off by "+str(abs(z-c)))

#   Play again?
replay=True
#No=False
#Yes=True
while replay:
    diceroller()
    again=input("Play again? Y/N: ")
    if again=="N":
        replay=False
    else:
        diceroller()
