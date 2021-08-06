import random
playerWin = 0
computerWin = 0
Tie = 0

moveslist = ['Rock','Paper','Scissors']
while True:
    print('1.Rock')
    print('2.Paper')
    print('3.Scissors')
    print('4.See Move Data')
    print('5.Show Win Loss Record')
    move = int(input('Enter a Number: '))
    print('')

    if move == 1:
        moveslist.append('Rock')
    elif move == 2:
        moveslist.append('Paper')
    elif move == 3:
        moveslist.append('Scissors')
    elif move == 4:
        print(moveslist)
    elif move == 5:
        print('Player Wins:',playerWin)
        print('Computer Wins:',computerWin)
        print('Ties:',Tie)
        print('')


    #Generate Random Move. Moves that players are more likely to use are also more likely to be selected
    rand = random.randint(0, (len(moveslist)-1))
    #use the generated random number to have the computer predict which move the player is likely to use
    computerPrediction = moveslist[rand]

    #Decide which move the computer is going to use based on prediction
    if computerPrediction == 'Rock':
        computerMove = 2
    elif computerPrediction == 'Paper':
        computerMove = 3
    elif computerPrediction == 'Scissors':
        computerMove = 1

    #Check Win
    if move == 1 and computerMove == 3 or move == 2 and computerMove == 1 or move == 3 and computerMove == 2:
        print('Player Win')
        print('')
        playerWin += 1
    elif computerMove == 1 and move == 3 or computerMove == 2 and move == 1 or computerMove == 3 and move == 2:
        print('Computer Wins')
        print('')
        computerWin += 1
    elif move == computerMove:
        print('Tie')
        print('')
        Tie += 1
