import random
from enum import Enum

class Scorecard(Enum):
    Wins = 0
    Losses = 1
    Ties = 2

class Moves(Enum):
    Rock = 0
    Paper = 1
    Scissors = 2

record = [0,0,0]

print('ROCK, PAPER, SCISSORS')

print(str(record[Scorecard.Wins.value]) + ' Wins, ' + str(record[Scorecard.Losses.value]) + ' Losses, '\
        + str(record[Scorecard.Ties.value]) + ' Ties')
        
move = input('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit\t')
print('')

while move != 'q':

    cpu_move = random.randint(Moves.Rock.value,Moves.Scissors.value)

    if move == 'r':
        print('Rock versus...')
        print(Moves(cpu_move).name)

        if Moves.Rock.value == cpu_move:
            print('It is a tie')
            record[Scorecard.Ties.value] = record[Scorecard.Ties.value] + 1

        elif Moves.Paper.value == cpu_move:
            print('You Lose')
            record[Scorecard.Losses.value] = record[Scorecard.Losses.value] + 1
        
        else:
            print('You Win')
            record[Scorecard.Wins.value] = record[Scorecard.Wins.value] + 1

    elif move == 'p':
        print('Paper versus...')
        print(Moves(cpu_move).name)

        if Moves.Paper.value == cpu_move:
            print('It is a tie')
            record[Scorecard.Ties.value] = record[Scorecard.Ties.value] + 1

        elif Moves.Scissors.value == cpu_move:
            print('You Lose')
            record[Scorecard.Losses.value] = record[Scorecard.Losses.value] + 1
        
        else:
            print('You Win')
            record[Scorecard.Wins.value] = record[Scorecard.Wins.value] + 1

    
    elif move == 's':
        print('Scissors versus...')
        print(Moves(cpu_move).name)

        if Moves.Scissors.value == cpu_move:
            print('It is a tie')
            record[Scorecard.Ties.value] = record[Scorecard.Ties.value] + 1

        elif Moves.Rock.value == cpu_move:
            print('You Lose')
            record[Scorecard.Losses.value] = record[Scorecard.Losses.value] + 1
        
        else:
            print('You Win')
            record[Scorecard.Wins.value] = record[Scorecard.Wins.value] + 1

    else:
        print('Invalid entry')
    
    print(str(record[Scorecard.Wins.value]) + ' Wins, ' + str(record[Scorecard.Losses.value]) + ' Losses, '\
        + str(record[Scorecard.Ties.value]) + ' Ties')

    move = input('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit\t')
    print('')
