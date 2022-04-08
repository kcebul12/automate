import random

def guess_number(answer):
    '''Takes a random number between 1 - 20 as an argument
    and continually narrows down the users guess until correct.
    Once the guesser guesses correctly, we tell them how many guesses it took'''

    count = 0
    guess = ''
    while guess != answer:

        count += 1
        
        guess = input('Take a guess.\n')
        guess = int(guess)
        if guess > answer:
            print('Your guess is too high')

        elif guess < answer:
            print('Your guess is too low')

        else:
            print('Good Job! You guessed my number in %d guesses' % count)
    
answer = random.randint(1,20)    

print('I am thinking of a number between 1 and 20')

guess_number(answer)
