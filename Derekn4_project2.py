#Derek Nasawang
#TCSS 142
#Project 2
import random
import sys




def nimSumFunc(stoneList):
#We are going to make a copy of the stoneList so that we are sure that it wont interfere with the board
    stoneList2 = stoneList[:]
    stoneList3 = []
    pileNum = max(stoneList2)
    nim = 0
    nimSum_1 = 0

#Hint step
#First we are going to calculate the nimSum
#The precodition is the number of stones all stored in a list
#The post-condition is the nimSum.
#To calculate how many stones to remove from the pile. 

#This for loop first iterates through the stoneList copy containing our stones.
#It appends to the next list in order to protect our list from being changed
#The second forloop will remove the highest number or the MAX in the list and remove it and set it to pileNum
#The third forloop will obtain the nimsum of the rest of the numbers without the highest number.
    for stone_1 in stoneList2:
        nim = nim ^ stone_1
        stoneList3.append(stone_1)
       
    for stone_2 in stoneList3:
        if stone_2 == pileNum:
            stoneList3.remove(pileNum)
            
    for stone_3 in stoneList3:
        nimSum_1 = nimSum_1 ^ stone_3
    
    
#Remove the correct amount of stones for the hint
    removeStones = pileNum - nimSum_1
    pile_Remove_from = stoneList.index(max(stoneList))
    #noNegRemoveStones = abs(removeStones)
    print("Nim Sum is: {}".format(nim))
    print("Hint: remove {} from pile: {}".format(removeStones, pile_Remove_from + 1))
#The number of stones to remove is the original number
#(The Original Number in the pile) - (nimSum of the other pile)
    


    
def updateBoard(player1, player2, stoneList):
    #Step 4
    #The pre-condition is its expecting the altered stoneList or the number of stones that were changed for each Pile
    #The post-condition is that it prints the gameboard with the updated number of stones.
    print("This is your board now: ")
    pileCount1 = 0
    print("-" * 30)
    for stones in stoneList:
        pileCount1 += 1
        print("pile {}: {}".format(pileCount1, "O" * stones))
    print("-" * 30)
    
    
        


def playerTurn(player1, player2, stoneList, pileRand, pileCount, winSum):
    #Step 3
    #The pre-condition is that the stoneList is passed here with no moves done to it
    #The post-condition is that the stoneList has been altered with the moves that player 1 and 2 make.
    #Ask player 1 for the move, the pile number and the number of stones to remove.
    #You need to make sure that if the user enters something invalid,
    #whether the pile of the stone number, you ask for the input again until
    #valid input is entered.
    #playerTurn is the players turn, 0 = player1, 1 = player2
    playerTurn_1 = player1
    while playerTurn_1:
        #print(stoneList)
        playerMovePile = input("{} what pile would you like to select?: ".format(playerTurn_1))
        playerMoveStone = input("How many stones would you like to remove?: ")
        #input validation to make sure they cant select a pile that exceeds the number of piles
        if playerMovePile.isalpha():
            if playerMoveStone.isalpha():
                print("invalid Choice")
        elif int(playerMovePile) > pileCount:
            print("Invalid Choice")
        elif(int(playerMoveStone) > stoneList[int(playerMovePile) - 1]):
            print("invalid Choice")
        else:
            stoneList[int(playerMovePile) - 1] = stoneList[int(playerMovePile) - 1] - int(playerMoveStone)
            winSum = winSum - int(playerMoveStone)
            
            
        #print(stoneList)
        updateBoard(player1, player2, stoneList)
        #Printing out the Sum for debugging purposes2
        #print("Win Sum", winSum)
        #Winsum meaaures to see if the sum of all of the stones i 0, if it is, it declares the winner
        
        if winSum == 0:
            print("{} You win!".format(playerTurn_1))
            playAgain = input("Do you want to play again? Enter Y for yes, anything for No: ")
            if playAgain == "Y" or playAgain == "y":
                main()
            else:
                sys.exit(0)
        #if the player move is a digit and the player move pile is less than the total pile count
        #then set the player 1 to player else  if the player is player 1 set it back to player 1
        if playerMovePile.isdigit() and (int(playerMovePile) <= pileCount):
            if playerTurn_1 == player1:
                playerTurn_1 = player2
            else:
                playerTurn_1 = player1
        nimSumFunc(stoneList)
        
        #playerTurn(player1, player2, stoneList, pileRand, pileCount, nimSum)
    
                
            
        
        

def nimBoard(player1, player2, stoneList):
    #Step 2
    #The pre-condition is that it is expecting an empty Stone List with player names established.
    #The post-condition is for it to pass out a stoneList. 
    #use a random number generator to generate between 2 to 5 piles
    #use a random number generator to generate between 1 to 8 stones
    #Display the Board in the following fashion:
    #Pile 1: O O O
    #Pile 2: O
    #Pile 3: O O
    #Pile 4: O O O O O O O O
    print("--" * 40)
    
    print("""_    _      _                            _                _            
| |  | |    | |                          | |              (_)           
| |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___    _ __  _ _ __ ___   
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | '_ \| | '_ ` _ \  
\  /\  /  __/ | (_| (_) | | | | | |  __/ | || (_) | | | | | | | | | | | 
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  |_| |_|_|_| |_| |_| 
                                                                        
                                                                        """)


    
    print("---" * 40)
    winSum = 0
    pileRand = random.randint(2, 5)
    pileCount = 0
    for pile in range(pileRand):
        #For the pine in range 0 to pilerand which is the rando integer generated.
        #The pileCount was created for counting the pile from 1
        #The stone random variable stores a number from 1 - 8 within the pile loop
        #and is multiplied to the pile count with the "O" String
        #all this information will then pass to playerTurn
        pileCount += 1
        stoneRand = random.randint(1, 8)
        stoneList.append(stoneRand)
        winSum += stoneRand
        print("pile {}:".format(pileCount), "O" * stoneRand)
    nimSumFunc(stoneList)
    playerTurn(player1, player2, stoneList, pileRand, pileCount, winSum)
    
    
    
    

def main():
    stoneList = []
    #Step 1
    #Asks players for name
    player1 = input("Enter name for player1: ")
    player2 = input("Enter name for player2: ")
    nimBoard(player1, player2, stoneList)
    #nimSum(stoneList)
    #playerTurn(player1, player2, stoneList)
        

main()
