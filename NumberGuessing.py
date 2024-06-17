from random import randint
from math import log

def guessing_game(lower_bound,upper_bound):
    no_of_guesses = 0
    random_number = randint(lower_bound,upper_bound)
    minimum_guess = round(log(upper_bound-lower_bound+1,2))
    print(f"You have {minimum_guess+1} chances to guess")

    while no_of_guesses <= minimum_guess:
        no_of_guesses+= 1
        user_guess = int(input("Guess the number: "))
        if user_guess == random_number:
            print(f"Congratulations! You did it in {no_of_guesses} try")
            break
        elif random_number < user_guess < upper_bound:
            print("Try Again! You guessed too high")
        elif lower_bound < user_guess < random_number:
            print("Try Again! You guessed too low")
        else:
            print("Invalid Guess")
            break
    
    if no_of_guesses > minimum_guess:
        print(f"Better luck next time!\n The number is {random_number}")
    print("Game Ended!")
    return


def main():
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    guessing_game(lower_bound, upper_bound)
        

if __name__ == "__main__":
    main()