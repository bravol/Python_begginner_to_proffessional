from game_data import  data
import random

# format data function
def format_data(account):
    """Takes the account data and returns the printable format"""
    # data is in dictionary
    account_name = account["name"]
    account_desc = account['description']
    account_country = account["country"]
    return f"{account_name}, a {account_desc}, from {account_country}"


def check_answer(user_guess, a_followers, b_followers):
    """Take a user's guess and the follower counts and return if they got it right"""
    if a_followers > b_followers:
        return user_guess == 'a'
    else:
        return user_guess == "b"

# break down a bigger problem into small pieces
# 1 Display art
score = 0
game_should_continue = True
# Generate a random account from the game data
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:
    # Generate a random account from the game data
    #  Making accounts for position B become the next account at position A on the next round
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)


    # format the account data into printable format
    print(f"compare A: {format_data(account_a)}.")
    print(f"Against B: {format_data(account_b)}.")

    # Ask user for a guess.
    guess = input("Who has more followers A or B: ").lower()
    # clear the screen
    print("\n" * 20)
    ## Get a follower account of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # check if the user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    ## Use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}")
    else:
        print(f"No that's wrong! Current score: {score}")
        game_should_continue = False
    # give a user feedback on their guess

    # Make the game repeatable.

