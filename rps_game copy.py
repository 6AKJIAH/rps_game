print("Print rock, paper or scissors")
human_turn = input ("human_turn:")
computer_turn = input ('Computer_turn:')

if human_turn == 'rock' and computer_turn == "scissors":
    print('Human wins!')
elif human_turn == 'paper' and computer_turn == "rock":
    print('Human wins!')
elif human_turn == 'scissors' and computer_turn == "paper":
    print('Human wins!')
elif human_turn == computer_turn:
    print('Draw!')
else:
    print("Computer wins!")