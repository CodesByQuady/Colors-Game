#This program will allow you to guess what color the cpu is thinking of.

import random, sys
rC = random.randint(0,4) #The randint() will choose a number betwwen 0-4 and return the value to rC 'random color'.

colorsList = ['Red','Blue','Green','Yellow','Orange']

cpu_color = colorsList[rC] #since rC will be assigned an intger number, it can be assigned to the index of the colorsList. List indexes are integers.

print("""
Welcome to the guessing colors game.
This game is very simple, I will give you
a list of colors.

All you have to do is guess the right color,
and you win $25.00

Lose, and you lose $25.00

You get 3 tries

Best of luck to you.

""")
for i in colorsList:
    print(i,'- ', end='') #This prints the elements in the list to the screen.
    
def colorGame():
    counter = 1
    wins = 0
    loss = 0
    money = 0.00
    attempt = 1
    while counter <=3:
        print('[Attempt:',attempt,']')

        guess = input('Enter Guess Here: ')

        if guess != cpu_color: #If the color isn't right, the game will loop again until the color is chosen.
            attempt += 1
            counter += 1
            print('You did not guess the right color, try again.')
            continue
        
        if attempt > 3: #They can't guess the colors in the amount of tries given, the game is over and the user losses money.
            loss += 1
            money -= 25.00
            print('You did not guess the right color in the given attempts. Better luck next time.')
            print('Money Loss:',money)
            print('Wins:',wins,'Losses:',loss)
            sys.exit()
            break
            

        else: #If the user guess the right color, then the game is over, and the user earns money.
            wins += 1
            money += 25.00
            print("Congrats, you've guessed the right color,", cpu_color)
            print('Money Won:',money)
            print('Wins:',wins,'Losses:',loss)
            sys.exit()
            
colorGame()



    

    

