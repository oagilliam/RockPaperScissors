#Created by: Olivia G.
#Completion date: 
#Prompt: Two player will enter one option out of rock, paper, and scissors. The winning player will be displayed.
#--Scissors beats paper.
#--Paper beats rock.
#--Rock beats scissors.

import random
import sys
    
while True:
    rps_dict = {'1': 'rock', '2':'paper', '3':'scissors'}
    #This section checks to see if the player entered an option of rock, paper, or scissors. 
    player = input('Select rock(1), paper(2), or scissors(3):')
    for key in rps_dict:
        if player in rps_dict:
            play_val = rps_dict.get(key)
            print('This is the value:' + play_val)
            break
        elif player not in rps_dict:
            print(type(player))
            print('Error! Not an option!')
            sys.exit()
    
    #This section compares the player's option with the computer's option. 
    r = 'rock'
    p = 'paper'
    s = 'scissors'
    comp_rps = random.choice(list(rps_dict.values()))
    comp = comp_rps
    
    if comp == r and play_val == p or comp == p and play_val == s or comp == s and play_val == r:
        print(play_val)
        print('You win! Computer picked ' + comp)
        break
    elif comp == r and play_val == s or comp == p and play_val == r or comp == s and play_val == p:
        print(play_val)
        print('You lose! Computer picked ' + comp)
        break
    elif comp == r and play_val == r or comp == p and play_val == p or comp == s and play_val == s:
        print(play_val)
        print('Game tied! Computer picked ' + comp)
        break
