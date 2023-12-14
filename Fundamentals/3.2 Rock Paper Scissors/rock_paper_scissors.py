import random

choices = ['rock', 'paper', 'scissors']
playerOutcomeMatrix = {
    'rock':     {'rock': 'TIE',  'paper': 'WIN',  'scissors': 'LOSE'},
    'paper':    {'rock': 'LOSE', 'paper': 'TIE',  'scissors': 'WIN'},
    'scissors': {'rock': 'WIN',  'paper': 'LOSE', 'scissors': 'TIE'}
}

computer_choice = random.choice(choices)
user_choice = input('Do you want rock, paper, or scissors?\n').lower()

if user_choice in choices:
    outcome = playerOutcomeMatrix[computer_choice][user_choice]
    print(f'You {outcome}! The computer chose {computer_choice}.')
else:
    print('Invalid choice. Please choose rock, paper, or scissors.')