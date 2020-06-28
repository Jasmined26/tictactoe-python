#This is my program to create a tic-tac-toe game.
#JJenkins

#Asks Player 1 to enter name
player1 = input("Player 1 please enter your name: ")
#Asks Player 2 to enter name
player2 = input("Player 2 please enter your name: ")
#Prints new line
print()

#Creates 2D list to create the game board
list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#Creates a 2D list with the possible winning outcomes
win1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [1, 4, 7], [2, 5, 8], [3, 6, 9]]
#Creates an empty list to store player 1's choices
player1list = []
#Creates an empty list to store player 2's choices
player2list = []

#Main function
def main():
    #Calls the create board function
    create_board()
    #Calls the gameplay function
    game_play()    

#Check Win function with parameter for the player list
def check_win(pList):
    #Loops through each list in the list of possible win combinations
    for table in win1:
        #Creates a counter to store the number of matches in each list
        matches = 0
        #Loops through each element in the current list
        for element in table:
            #If the current element is also in the player's list of choices,
            #increment matches by 1
            if element in pList:
                matches = matches + 1
        #If all three elements in the win combination are in the player's
        #list of choices, return True.
        if matches == 3:
            return True
    
#Create Game Board function
def create_board():
    #Loops through each number in the range of the game board list
    for number in range(len(list1)):
        #Prints a vertical bar in front of each game space
        print(' | ', end='')
        #Loops through each index in the list
        for index in list1[number]:
            #Prints the number indented 3 spaces and prints
            #a vertical bar at the end
            print("%3s" % index, end='   | ')
        #prints a new line
        print()
        #Prints a dashed line after the first and second row of the game
        #board
        if number < 2:
            print("-" * 27)
        
#Game play function
def game_play():
    #Sets a counter to store how many turns the players have had
    i = 1
    #Loops through each number in the range of the total number of choices
    for number in range(9):
        #If the number is even, it is player 1's turn
        if number % 2 == 0:
            print() #Prints a new line 
            print(player1, end=' ') #Print player 1's name
            #Prompts the user to enter their choice, converts it to a
            #variable, and creates a variable that stores it
            playerInput = int(input("pick a number: "))
            #Appends the player's choice to their list of choices
            player1list.append(playerInput)
            #Loops through each list that makes up the game board
            for table in list1:
                #If the player's choice is in the current list, replaces that position
                #with an 'X'
                if playerInput in table:
                    #Creates a variable that stores the index that contains
                    #the player's choice
                    choice = table.index(playerInput)
                    #Changes the index to 'X'
                    table[choice] = "X"
            #If the player is on their 3rd or above turn, use the win function to see
            #player 1 has won yet
            if i >= 3:
                win = check_win(player1list) #calls check_win function
                #If check_win returns True, Player 1 has won.
                if win == True:
                    print()
                    create_board()
                    print()
                    print(player1, "you have won!")
                    #Returns true to exit the loop
                    return True
        #If the number is odd, it is player 2's turn
        else:
            print() #Prints a new line
            print(player2, end=' ') #PRints player 2's name
            #Prompts the user to enter their choice, converts it to a
            #variable, and creates a variable that stores it            
            playerInput = int(input("pick a number: "))
            #Appends the player's choice to their list of choices
            player2list.append(playerInput)
            #Loops through each list that makes up the game board
            for table in list1:
                #If the player's choice is in the current list, replaces that position
                #with an 'O'                
                if playerInput in table:
                    #Creates a variable that stores the index that contains
                    #the player's choice                    
                    choice = table.index(playerInput)
                    #Changes the index to 'O'
                    table[choice] = "O"
            #If the player is on their 3rd or above turn, use the win function to see
            #player 2 has won yet            
            if i >= 3:
                win = check_win(player2list)#calls check_win function
                #If check_win returns True, Player 2 has won.
                if win == True:
                    print()
                    create_board()  
                    print()
                    print(player2, "you have won!")
                    #Returns true to exit the loop
                    return True            
        print()
        create_board()
        #If the player's have completed their last turn and no one
        #has won, prints that there is no winner.
        if (i == 9) and (win != True):
            print()
            print("Oops! No winner!")
        i = i + 1


#Calls main function
main()