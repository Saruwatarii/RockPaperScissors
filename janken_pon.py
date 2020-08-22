'''
Program so far: An unfair version.
1. Take an input from the user
2. Find an option that wins over the user's option
3. Output a line : Sorry, but the computer chose {option}
'''


scissors = "scissors"
rock = "rock"
paper = "paper"
user = input()

if user == "scissors":
    print(f"Sorry, but the computer chose {rock}")
elif user == "rock":
    print(f"Sorry, but the computer chose {paper}")
elif user == "paper":
    print(f"Sorry, but the computer chose {scissors}")