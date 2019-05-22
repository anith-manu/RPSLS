### Solution to Arnold Clark Hack Day Challenge 2019 ###


import random


# Converts choice to number
def choice_to_number(name):
    
    if(name == 'ROCK'):
        return 0;
    elif(name == 'SPOCK'):
        return 1;
    elif(name == 'PAPER'):
        return 2;
    elif(name == 'LIZARD'):
        return 3;
    elif(name == 'SCISSORS'):
        return 4;
    else:
        print ("Invalid choice!")
        
          
# Converts number to choice
def number_to_choice(number):
    
    if(number == 0):
        return 'ROCK';
    elif(number == 1):
        return 'SPOCK';
    elif(number == 2):
        return 'PAPER';
    elif(number == 3):
        return 'LIZARD';
    elif(number == 4):
        return 'SCISSORS';
    else:
        print ("Invalid choice!")
        
        
def playGame(number): 

    print ("\n")
   
    # computers choice
    compNumber = random.randrange( 0, 4 )
    
    print ("You chose " + number_to_choice(number))
    print ("Computer chose " + number_to_choice(compNumber))
    
    # compute and display winner
    difference = (compNumber - number) % 5
    
    if( difference == 1 or difference == 2 ):
        print ("Computer wins!")
    elif ( difference == 4 or difference == 3 ):
        print ("You win!")
    elif( difference == 0 ):
        print ("Draw!")
        
           
##### MAIN #####
repeat = "y"

while repeat=="y":
    choice = input("""
                      0: Rock
                      1: Spock
                      2: Paper
                      3: Lizard
                      4: Scissors

                      Please enter a number: """)
   
    playGame(int(choice))
    repeat = input("\nWould you like to play again? (y/n) \n")

    
    


