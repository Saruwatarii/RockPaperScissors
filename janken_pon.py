'''
Program so far: lose, draw and win provided from the computer and the user input.
1. Take an input from the user
2. computer chooses a random option
3. Compare the option from the computer and the user to determine the possible winner
4. Out put status depending on the game: Win, Lose or Draw
'''
import random
import sys

class JankenPon:
    def __init__(self):
        self.computer = ['rock', 'paper', 'scissors']
        self.com_opt = random.choice(self.computer)
        self.user_winner = {'rock': 'scissors',
                            'paper': 'rock',
                            'scissors': 'paper'}
        self.endless_loop = '!exit'

    def win(self):
        print(f"Well done. The computer chose {self.com_opt} and failed")
        self.computer_opt()
        self.game_start()

    def lose(self):
        print(f"Sorry, but the computer chose {self.com_opt}")
        self.computer_opt()
        self.game_start()

    def draw(self):
        print(f"There is a draw ({self.com_opt})")
        self.computer_opt()
        self.game_start()

    def invalid_input(self):
        print(f"Invalid unput")
        self.game_start()

    def game_state(self):
        while self.user_option != self.endless_loop:
            if self.user_option == self.com_opt:
                self.draw()

            elif self.user_option in self.computer:
                if self.user_winner[self.user_option] == self.com_opt:
                    self.win()
                else:
                    self.lose()
            elif self.user_option not in self.computer:
                self.invalid_input()
        else:
            print("Bye!")
            sys.exit()

    def computer_opt(self):
        self.com_opt = random.choice(self.computer)

    def game_start(self):
        self.user_option = input()
        self.game_state()

    def game_intro(self):
        print("Welcome to the Janken pon game: please choose between (rock, paper or scissors): ")


game_start = ""
JankenPon.game_intro(game_start)

user = JankenPon()
user.game_start()

