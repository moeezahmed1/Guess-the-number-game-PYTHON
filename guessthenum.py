# Mini Guess the number Game

import random


def guess_the_number():
    # Python will give us a random number to guess
    number_to_guess = random.randint(1,100)
    attempts = 0

    print('Guess the number between 1 And 100')
    print('Type quit, If you want to end this game')
    print()

    
    while True:
        user_guess = input('Enter your Guess: ')

        if user_guess.lower() == 'quit':
            print('Thanks For Playing')
            break

        try: 
            user_guess = int(user_guess)

        except ValueError:
            print('Invalid Input! Enter A Whole Number')
            continue

        attempts += 1    


        if user_guess == number_to_guess:
            print(f'Congratulations!!! You Guessed The Correct Number In {attempts} Attempts')
            break

        elif user_guess < number_to_guess:
            print('Too Low! Try Again')
        else:
            print('Too High! Try Again')

if __name__ == '__main__':
    guess_the_number()                
                 
