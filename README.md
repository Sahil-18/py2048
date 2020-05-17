# py2048

This project is a part of VNIT's IVLabs Summer Internship Progamme. This game is developed using Python language.This game is customised version of original 2048 game.

## Game Discription

This game uses matrix as game board in which initially all position are as '0' and any one random position as '2'. This game uses command line arguments to change the value of 'n' i.e. matrix size or dimension and 'w' i.e. winning number. These inputs has to be provided while starting the game. If user forgot to enter the command line argument,then these arguments accepts default value from programme i.e. n=5, w=2048. If user inputs incorrect value of w i.e. 12 or 24, its value will be changed to smaller value than user input but equal to 2^p where p is an integer. e.g. if user input w=12, then it will be changed to w=8. User can end the game in between by providing input as 'e' or 'E'. In this game while providing input, no need to press 'Enter' again and again. 

## Running The Game
### On Windows OS 
To start the game and change the arguments, enter the following command 
### python 2048.py --n 4 --w 16
These command run the game with n=4 and w=16. 

### User input and its movement discription
w/W = UP

a/A = LEFT

s/S = DOWN

d/D = RIGHT

e/E = END THE GAME

After every valid move, game board is updated and '2' is added at any random position where there was '0'. If move input is valid but there is no change in game board means these move is invalid at that moment and insertion of '2' will not be done. If user enter invalid input, it will show invalid move message and insertion of '2' will not be done.

### Win Defeat instructions
If value at any one of the matrix position is equal to 'w' (winning number), program will prompt winning message and game ends here. If these condition is not satisfied, then program is passed to check defeat condition. If there are no posible move, it will prompt loosing message and game ends or it will ask for next move.

My programme runs on Windows OS so please run it on Windows. I don't have any medium to check that it can run on Ubuntu as well.
