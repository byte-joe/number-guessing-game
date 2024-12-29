#Number guessing game project
import random                                   #random module to generate a random number

print("Welcome! to the number guessing game")

secretNumber = random.randint(1, 10)            #generate number within specifed range
counter = 0                                     #counter variable to keep track of user inputs

while True:                                     #while loop will loop until the user guesses the correct number
    userGuess = int(input("Enter your guess: "))
    counter += 1
    if userGuess < secretNumber:
        print("Too low!")
    elif userGuess > secretNumber:
        print("Too high!")
    else:
        print(f"You've won in {counter} attempts!")
        break                                   #breaks the loop once user has guessed the correct number
print(f"The correct number was {secretNumber}!")