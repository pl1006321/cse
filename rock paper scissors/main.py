import random

def generator():
  play = random.randint(1, 3)
  # 1 is rock, 2 is paper, 3 is scissors
  return(play)

def play_again():
  choice = str(input('Would you like to play again? Enter yes or no: '))
  choice = choice.strip()
  choice = choice.lower()
  if choice == 'yes': 
    return(1)
  if choice == 'no':
    return(0)

draw = 1
while bool(draw):
  player = str(input('Please enter your choice of rock, paper, or scissors: '))
  player = player.strip()
  player = player.lower()
  program = generator()
  if player != 'rock' and player != 'paper' and player != 'scissors':
    print('Please enter a valid input.')
    draw = 1
  else:
    if player == 'rock': 
      if program == 2: 
        print('The computer chose paper! You\'ve lost!')
        play_again()
      elif program == 3:
        print('The computer chose scissors! You\'ve won!')
        play_again()
      else: 
        print('The computer chose rock too! It\'s a draw!')
        draw = 1
    if player == 'paper':
      if program == 1: 
        print('The computer chose rock! You\'ve won!')
        play_again()
      elif program == 3:
        print('The computer chose scissors! You\'ve lost!')
        play_again()
      else: 
        print('The computer chose paper too! It\'s a draw!')
        draw = 1
    if player == 'scissors':
      if program == 1:
        print('The computer chose rock! You\'ve lost!')
        play_again()
      elif program == 2:
        print('The computer chose paper! You\'ve won!')
        play_again()
      else: 
        print('The computer chose scissors too! It\'s a draw!') 
        draw = 1
