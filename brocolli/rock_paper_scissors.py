""" A game of rock paper scissors, computer selects randomly from rock, paper or scissors
NOTE : All input must be lowercase """
import random
rps = ['rock', 'paper', 'scissors']
player = ''     # string
player_score = 0
cpu_score = 0

while True:
    computer = random.choice(rps)
    player = input('\nEnter your choice, Rock, Paper or Scissors ? type (end) to stop game ')
    if player == computer:
        print("Tie! Game on ")

    elif player == 'paper':
        if computer == 'scissors':
            print('computer cuts player, computer chose scissors')
            cpu_score += 1
        else:
            print('You covered computer, computer chose rock')
            player_score += 1
        print(f'Player {player_score} Vs Computer {cpu_score}')

    elif player == 'rock':
        if computer == 'paper':
            print('Computer covered You, computer chose rock')
            cpu_score += 1
        else:
            print('You smashed computer, computer chose scissors')
            player_score += 1
        print(f'Player {player_score} Vs Computer {cpu_score}')

    elif player == 'scissors':
        if computer == 'rock':
            print('Computer smashes you, computer chose rock')
            cpu_score += 1
        else:
            print('You cut computer, computer chose paper ')
            player_score += 1
        print(f'Player {player_score} Vs Computer {cpu_score}')

    elif player == 'end':
        print('Final scores')
        print(f'Player {player_score} Vs Computer {cpu_score}')
        break