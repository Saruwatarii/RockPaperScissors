'''
Program so far: lose, draw and win provided from the computer and the user input Greeting the user and chowing the
the current score the different players.
1. Take an input from the user, Greet the User.
2. computer chooses a random option.
3. Compare the option from the computer and the user to determine the possible winner.
   Can also choose !rating to check score.
4. Out put status depending on the game: Win, Lose or Draw. If the user input something other that the given arguments,
   "Invalid put" will be shown
'''
import random
import sys

class JankenPon:
    soccer = 0

    def __init__(self):
        self.user_option = None
        self.computer = ['rock', 'paper', 'scissors']
        self.com_opt = random.choice(self.computer)
        self.user_winner = {'rock': 'scissors',
                            'paper': 'rock',
                            'scissors': 'paper'}
        self.endless_loop = '!exit'
        self.each_rating = "!rating"
        self.rate_score = None
        self.game_name = None

    def win(self):
        print(f"Well done. The computer chose {self.com_opt} and failed")
        JankenPon.soccer += 100
        self.computer_opt()
        self.game_start()

    def lose(self):
        print(f"Sorry, but the computer chose {self.com_opt}")
        self.computer_opt()
        self.game_start()

    def draw(self):
        print(f"There is a draw ({self.com_opt})")
        JankenPon.soccer += 50
        self.computer_opt()
        self.game_start()

    def invalid_input(self):
        print(f"Invalid unput")
        self.game_start()

    def rating(self):
        print(f"Your rating: {JankenPon.soccer}")
        self.game_start()

    def game_state(self):
        if self.user_option == self.com_opt:
            self.draw()

        elif self.user_option in self.computer:
            if self.user_winner[self.user_option] == self.com_opt:
                 self.win()
            else:
                self.lose()

        elif self.user_option == self.each_rating:
            self.rating()

        elif self.user_option not in self.computer:
            self.invalid_input()

    def computer_opt(self):
        self.com_opt = random.choice(self.computer)

    def game_start(self):
        self.user_option = input()
        while self.user_option != self.endless_loop:
            self.game_state()
        else:
            print("Bye!")
            sys.exit()

    def game_intro(self):
        print("Welcome to the Janken pon game: please choose between (rock, paper or scissors): ")

    def introduction(self):
        self.game_name = input("Enter your game name: ")
        print(f"Hello, {self.game_name}")
        self.score_text = open("score.txt", "r")
        for line in self.score_text:
            if self.game_name in line:
                JankenPon.soccer = int(line.split()[1])
        self.score_text.close()

game_start = ""
JankenPon.game_intro(game_start)

user = JankenPon()
user.introduction()
user.game_start()

