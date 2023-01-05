from higherlowerdata import data
import random


def check_account(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def format_account(account):
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country}"


score = 0
print('WELCOME TO THE HIGHER LOWER GAME CREATED BY LAKSHYA')
game_should_continue = True
account_b = random.choice(data)
while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_b == account_a:
        account_b = random.choice(data)
    print(f'Compare A: {format_account(account_a)}')
    print('V/S')
    print(f'Against B: {format_account(account_b)}')
    guess = input("Who has more followers? Type 'A' or 'B'").lower()
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    check_guess = check_account(guess, a_follower_count, b_follower_count)
    if check_guess:
        score += 1
        print(f'Well done you guess it correct {score}')
    else:
        game_should_continue = False
        print(f'Sorry you guessed it wrong your score is {score}')
