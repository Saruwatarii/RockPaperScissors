'''
Program so far: lose, draw and win provided from the computer and the user input.
1. Take an input from the user
2. computer chooses a random option
3. Compare the option from the computer and the user to determine the possible winner
4. Out put status depending on the game: Win, Lose or Draw
'''
import random

class JankenPon:
    def __init__(self, user_option):
        self.user_option = user_option
        self.computer = random.choice(['rock', 'paper', 'scissors'])
        self.user_winner = {'rock': 'scissors',
                            'paper': 'rock',
                            'scissors': 'paper'}

    def win(self):
        print(f"Well done. The computer chose {self.computer} and failed")

    def lose(self):
        print(f"Sorry, but the computer chose {self.computer}")

    def draw(self):
        print(f"There is a draw ({self.computer})")

    def game_state(self):
        if self.user_option == self.computer:
            self.draw()
        elif self.user_winner[self.user_option] == self.computer:
            self.win()
        else:
            self.lose()
    def game_intro(self):
        print("Welcome to the Janken pon game: please choose between (rock, paper or scissors): ")


game_start = ""
JankenPon.game_intro(game_start)

user_input = input()
user = JankenPon(user_input)
user.game_state()