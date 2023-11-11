import random, sys

print('rock','paper','scissors')

Wins = 0
Ties = 0
Losses = 0


while True:
    print("%s Wins, %s Ties , %s Losses,"% (Wins, Losses, Ties))
    while True:
        print('Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print('Type one of r, p, s, or q')

        if playerMove == "r":
            print('Rock Versus...')
        elif playerMove == "p":
            print('Paper Versus...')
        elif playerMove == "s":
            print('Scissors Versus...')

        randomNumber = random.randint(1, 3)
        if randomNumber == 1:
            computerMove = 'r'
            print("ROCK")
        elif randomNumber == 2:
            computerMove = 'p'
            print("PAPER")
        elif randomNumber == 3:
            computerMove = 's'
            print("SCISSORS")

        if playerMove == computerMove:
            print("It is tie...")
            Ties = Ties + 1
        elif playerMove == 'r' and computerMove == 's':
            print('You Win...')
            Wins = Wins + 1
        elif playerMove == "p" and computerMove == 'r':
            print('You Win...')
            Wins = Wins + 1
        elif playerMove == "s" and computerMove == 'p':
            print('You Win...')
            Wins = Wins + 1

        elif playerMove == "r" and computerMove == 'p':
            print('You Lose...')
            Losses = Losses + 1
        elif playerMove == "p" and computerMove == 's':
            print('You Lose...')
            Losses = Losses + 1
        elif playerMove == "s" and computerMove == 'r':
            print('You Lose...')
            Losses = Losses + 1
        



            
