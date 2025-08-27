# This is a basic guessing game made using python
import random # importing the random package
n=random.randint(0,100) # This show that the guessing game has the limit to guess a number just between 0 to 100
a=-1
guesses=0 # initialised variable for storing value of number of guesses made by the user
while(a!=n):
    try:
        guesses+=1 # To update the number of guesses by each new guess
        a=int(input("Guess a number :- "))
        if(a>100):
            print("Your random number is just between 0 to 100, so kindly guess again.") # So user can play the game more properly by just guessing numbers between 0-100
        if(a>n):
            print("Nice Try! Think of a lower value number.") #If the guessed value is more than the actual value so this will pop
        elif(a<n):
            print("Woah Great Guess! But Think of a higher value number.") #If the guessed value is less than the actual value so this will pop
        else:
            print(f"Congratulations! You have correctly guessed it in {guesses} guesses.")
    except ValueError:
        print("Enter a valid number please")
        continue
