import random

def game(y):
    number = int(random.randint(1,100))
    attempts = int(y)
    count = int(1)
    print(f"\nYou have {attempts} attempt to guess my number\n")

    while count <= attempts:
        guess = int(input(f"Attempt {count} \nGuess for a number between 1 and 100\n-> "))

        if guess == number:
            return print(f"Correct, my number was {number}")
        
        elif guess > number:
            print("Too high\n")
            count += 1
        
        elif guess < number:
            print("Too low\n")
            count += 1
    
    if count>attempts:
        return print("GAME OVER. Out of attempts")

print("Welcome to Guess my number. You can select number of attempts you would like and we can start the game")
attempt = int(input("\nHow many attempts would you like to guess numbers from 1 to 100\n-> "))
game(attempt)
