#Created by: Olivia G.
#Completion date: 
#Prompt: Two player will enter one option out of rock, paper, and scissors. The winning player will be displayed.
#--Scissors beats paper.
#--Paper beats rock.
#--Rock beats scissors.

import random
import sys
    
while True:
    rps_dict = {1: 'rock', 2:'paper', 3:'scissors'}
    #This section checks to see if the player entered an option of rock, paper, or scissors. 
    for key in rps_dict:
        player = int(input('Select rock(1), paper(2), or scissors(3):'))
        if player in rps_dict:
            play_val = rps_dict[key]
            break
        elif player not in rps_dict:
            print(type(player))
            print('Error! Not an option!')
            sys.exit()
    
    #This section compares the player's option with the computer's option. 
    comp_rps = random.choice(list(rps_dict.values()))
    comp = comp_rps
    
    if comp == 'rock':
        if play_val == 'paper':
            print('You win! Computer picked '+ comp)
            break
        elif play_val == 'scissors':
            print('You lose! Computer picked '+ comp)
            break
        elif play_val == 'rock':
            print('Game tied! You and computer picked ' + comp)
            break
    elif comp == 'paper':
        if play_val == 'rock':
            print('You lose! Computer picked '+ comp)
            break
        elif play_val == 'scissors':
            print('You win! Computer picked '+ comp) 
            break
        elif play_val == 'paper':
            print('Game tied! You and computer picked ' + comp)
            break
    elif comp == 'scissors':
        if play_val == 'paper':
            print('You lose! Computer picked '+ comp)
            break
        elif play_val == 'rock':
            print('You win! Computer picked '+ comp)
            break
        elif play_val == 'scissors':
            print('Game tied! You and computer picked ' + comp)
            break