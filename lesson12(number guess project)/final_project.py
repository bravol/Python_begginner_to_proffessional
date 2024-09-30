import random

# GLOBAL CONSTANTS
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
# function to check user's guess against actual guess
def check_answer(user_guess, actual_answer, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        turns -= 1
        print("Too high.")
        return turns
    elif user_guess < actual_answer:
        turns -= 1
        print("Too low")
        return turns
    else:
        print(f"You got it! The answer was {actual_answer}")

# function to set difficulty/level
def set_difficulty():
    level = input("Choose a difficulty Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # choosing a number between 1 and 100
    print("Welcome to the number Guessing game! ")
    print("I'm thinking a number between 1 and 100. ")
    answer = random.randint(1,100)


    turns = set_difficulty()
    # let a user guess a number
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

# track the number of turns and reduce by 1 if they get it wrong
# repeat the guessing functionality if the answer is wrong

game()