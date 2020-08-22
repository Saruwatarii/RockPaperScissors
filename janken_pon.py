'''
Program so far: lose, draw and win provided from the computer and the user input.
1. Take an input from the user
2. computer chooses a random option
3. Compare the option from the computer and the user to determine the possible winner
4. Out put status depending on the game: Win, Lose or Draw
'''
import random
print("Welcome to the Janken pon game: please choose between (rock, paper or scissors): ")
computer = random.choice(['rock', 'paper', 'scissors'])
user_winner = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}
user = input()

if user == computer:
    print(f"There is a draw ({computer})")
elif user_winner[user] == computer:
    print(f"Well done. The computer chose {computer} and failed")
else:
    print(f"Sorry, but the computer chose {computer}")