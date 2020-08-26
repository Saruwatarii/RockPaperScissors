'''
Program so far: lose, draw and win provided from the computer and the user input Greeting the user and chowing the
the current score the different players Now the user can either choose to play the default
game(rock, paper and scissors) or with more options(total of 15 option).
The user can choose the option that will be used.
1. Take an input from the user (name), Greet the User. Tell the user to choose the different option, showing an example.
2. Output that the game will start and the computer chooses a random option from the options the user have chosen.
3. Compare the option from the computer and the user to determine the possible winner.
   Can also choose !rating to check score.
4. Out put status depending on the game: Win, Lose or Draw. If the user input something other that the given arguments,
   "Invalid put" will be shown.
'''
import random
import sys

class JankenPon:
    soccer = 0

    def __init__(self):
        self.user_option = None
        self.computer = ['rock', 'paper', 'scissors']
        self.more_computer = []
        self.options = "rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire"
        self.com_opt = random.choice(self.computer)
        self.user_winner = {'rock': ['scissors', "fire", "snake", "human", "tree", "wolf", "sponge"],
                            'fire': ['scissors', "paper", "snake", "human", "tree", "wolf", "sponge"],
                            'scissors': ['air', "paper", "sponge", "wolf", "tree", "human", "snake"],
                            'snake': ['water', "air", "paper", "sponge", "wolf", "tree", "human"],
                            'human': ['dragon', "air", "paper", "sponge", "wolf", "tree", "water"],
                            'tree': ['dragon', "air", "paper", "sponge", "wolf", "devil", "water"],
                            'wolf': ['dragon', "air", "paper", "sponge", "lightning", "devil", "water"],
                            'sponge': ['dragon', "air", "paper", "gun", "lightning", "devil", "water"],
                            'paper': ['rock', "gun", "lightning", "devil", "dragon", "water", "air"],
                            'air': ['rock', "gun", "lightning", "devil", "dragon", "water", "fire"],
                            'water': ['rock', "gun", "lightning", "devil", "dragon", "scissors", "fire"],
                            'dragon': ['rock', "gun", "lightning", "devil", "snake", "scissors", "fire"],
                            'devil': ['rock', "gun", "lightning", "human", "snake", "scissors", "fire"],
                            'lightning': ['rock', "gun", "tree", "human", "snake", "scissors", "fire"],
                            'gun': ['rock', "wolf", "tree", "human", "snake", "scissors", "fire"]
                            }
        self.endless_loop = '!exit'
        self.each_rating = "!rating"
        self.rate_score = None
        self.game_name = None

    def win(self):
        if self.specifying_option != "":
            print(f"Well done. The computer chose {self.more_com_opt} and failed")
        else:
            print(f"Well done. The computer chose {self.com_opt} and failed")

        JankenPon.soccer += 100
        self.computer_opt()
        self.game_start()

    def lose(self):
        if self.specifying_option != "":
            print(f"Sorry, but the computer chose {self.more_com_opt}")
        else:
            print(f"Sorry, but the computer chose {self.com_opt}")

        self.computer_opt()
        self.game_start()

    def draw(self):
        if self.specifying_option != "":
            print(f"There is a draw ({self.more_com_opt})")
        else:
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

    def open_file(self):
        self.score_text = open("score.txt", "r")
        for line in self.score_text:
            if self.game_name in line:
                JankenPon.soccer = int(line.split()[1])
        self.score_text.close()

    # default game option
    def game_state(self):
        if self.user_option == self.com_opt:
            self.draw()
        elif self.user_option in self.computer:
            for key_name in self.user_winner:
             #   print(self.user_winner[self.user_option])
                if self.com_opt in self.user_winner[self.user_option]:
                    self.win()
                else:
                    self.lose()
        elif self.user_option == self.each_rating:
            self.rating()
        elif self.user_option not in self.computer:
            self.invalid_input()
    # The option the user have chosen
    def game_state_new(self):
        if self.user_option == self.more_com_opt:
            self.draw()
        elif self.user_option in self.more_computer:
            for key_name in self.user_winner:
            #    print(self.user_winner[self.user_option])
                if self.more_com_opt in self.user_winner[self.user_option]:
                    self.win()
                else:
                    self.lose()
        elif self.user_option == self.each_rating:
            self.rating()
        elif self.user_option not in self.more_computer:
            self.invalid_input()
    # updating the computer choice after each round
    def computer_opt(self):
        if self.specifying_option != "":
            self.more_com_opt = random.choice(self.more_computer)
        else:
            self.com_opt = random.choice(self.computer)

    def game_start(self):
        self.user_option = input()
        while self.user_option != self.endless_loop:
            if not self.more_computer:
                self.game_state()
            else:
                self.game_state_new()
        else:
            print("Bye!")
            sys.exit()

    def game_intro(self):
        print("Welcome to the Janken pon game: ")

    def introduction(self):
        self.game_name = input("Enter your name: ")
        print(f"Hello, {self.game_name}\n")
        self.open_file()
        print("Enter blank if you want the default game (rock, paper, scissors)\nIf you want more option,"
              " please provide a list of option that is seperated by a comma.\n\n"
              "For example :  rock,fire,paper,water\n\n"
              "Below you see the full list of option\n")
        print(", ".join(self.options.split(",")),"\n")
        self.specifying_option = input("Enter here: ")
        if self.specifying_option == '':
            print("Okay default it is, let's start")
            self.game_start()
        else:
            self.helping = self.specifying_option.split(",")
            for option in range(len(self.helping)):
                self.more_computer.append(self.helping[option])
            self.more_com_opt = random.choice(self.more_computer)
            print("I see, you want a challenge. let's start")
            self.game_start()

user = JankenPon()
user.introduction()


