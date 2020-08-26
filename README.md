# RockPaperScissors
Rock, paper, scissors is a well-known hand game. Each one of two players simultaneously forms one of three shapes with their hands, and then, depending on the chosen shapes, the winner is determined: rock beats scissors, paper wins over rock, scissors beat paper. The game is widely used to make a fair decision between equal options. A more advanced version of the game with the 12 more option to it:
[rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire ] 
This version can be played against the computer.

The program:
1. Ask for the user name:`Enter your name`  and greet the the user with **Hello**, **<name>**
2. Read a file named `rating.txt` and check if the user name is in that file; if yes, the score from that file will be used. If no, the starting scorce will be 0.
3. Output: 
  
```Enter blank if you want the default game (rock, paper, scissors)

If you want more option, please provide a list of option that is seperated by a comma.

For example :  rock,fire,paper,water

Below you see the full list of option

rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire 
```

4. Output a line `Okay, let's start`
5. Play the game by writing in one option.
6. If input is incorrect, it outputs `Invalid input`, and start at nr 5.
7. If the input is !exit, the ouput  is `Bye!` and the game stop
8. If the input is one of the option, then the computer chooses a random option.
9. Output the result of the game like:
  - Lose -> `Sorry, butthe computer chose <option>`
  - Draw -> `There is a draw <option>`
  - Win -> "Well done. The computer chose <option> and failed.
10. The scoring system gets updated if the user gets draw or win, if the user loses nothing changes. For each win the score add 100 to the user score, and 50 if draw.
11. After a game, it starts again with the option the user choose in the beginning before starting the game.
  
  ## Example 
  
```  
Enter your name: Time
Hello, Time

Enter blank if you want the default game (rock, paper, scissors)
If you want more option, please provide a list of option that is seperated by a comma.

For example :  rock,fire,paper,water

Below you see the full list of option

rock, gun, lightning, devil, dragon, water, air, paper, sponge, wolf, tree, human, snake, scissors, fire 

Enter here: rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
I see, you want a challenge. let's start
fire
Well done. The computer chose tree and failed
fire
Well done. The computer chose snake and failed
fire
Sorry, but the computer chose water
fire
Well done. The computer chose snake and failed
fire
Well done. The computer chose snake and failed
fire
Sorry, but the computer chose rock
fire
Well done. The computer chose wolf and failed
water
Sorry, but the computer chose snake
water
Sorry, but the computer chose air
!rating
Your rating: 500
!exit
Bye!
```

