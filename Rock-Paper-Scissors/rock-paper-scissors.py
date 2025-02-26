import random

while True:
    print('1: Rock ✊, 2: Paper ✋, 3: Scissors ✌')
    player = int(input('Pick a number: '))
    if(player not in [1,2,3]):
      print('Invalid Input, Please enter 1,2, or 3')
    computer = random.randint(1,3)

    if((player == 1 and computer == 3) or (player == 3 and computer == 2) or (player == 2 and computer == 1)):
      print('You win')
    elif(player == computer):
      print('Its a tie')
    else:
      print('Computer won')

    play_again = input("Do you want to continue? (y/n): ").strip().lower()
    if play_again != 'y':
      break


