import random


def play_game():
    animals = [
    "Elephant", "Tiger", "Lion", "Cheetah", "Leopard", "Giraffe", "Zebra", "Kangaroo", "Panda", "Koala",
    "Rhinoceros", "Hippopotamus", "Gorilla", "Chimpanzee", "Sloth", "Armadillo", "Otter", "Fox", "Wolf", "Deer",
    "Moose", "Buffalo", "Crocodile", "Alligator", "Penguin", "Dolphin", "Whale", "Shark", "Octopus", "Eagle"
]
    attempts = 10
    word = random.choice(animals).lower()

    guessedWord = ['_'] * len(word) 

    while(attempts > 0):
        print('\nGuess the animal: ' + ' '.join(guessedWord))
        guess = input('Guess a letter: ').lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input! Please enter a single letter.")
            continue

        if guess in guessedWord:
            print("You've already guessed that letter!")
            continue

        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    guessedWord[i] = guess
            print('Yay great guess')
        else:
            attempts -= 1
            print('Wrong Guess ' + str(attempts) + 'left')
        if '_' not in guessedWord:
            print('Congratulations, You\'ve guessed the word: ' + word)
            break
    

    if '_' in guessedWord:
        print('You\'re out of attempts. The word was: ' + word)

def main_menu():
    while True:
        print("\nWelcome to the Animal Guessing Game!")
        print("1. Play Game")
        print("2. Exit")
        choice = input("Select an option (1 or 2): ").strip()

        if choice == '1':
            play_game()
        elif choice == '2':
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Invalid choice! Please select 1 or 2.")

if __name__ == "__main__":
    main_menu()
    
           

