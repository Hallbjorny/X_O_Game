#!/usr/bin/env python
# coding: utf-8

# In[ ]:


ind = True
#Checking if move is correct and registering it to the gametable
def make_move(gametable):
    global ind
    while True:
        try:
              row =int(input("row:"))
        except ValueError: 
            print ("That\'s not a number!")
        else:
            if row < 3: 
                break
            else:
                print ("Out of range. Try again")
        
    while True:
        try:
              line = int(input("line:"))
        except ValueError: 
            print( "That\'s not a number!")
        else:
            if line < 3: 
                break
            else:
                print ("Out of range. Try again")
                
    if gametable[line][row]=="-":
       gametable[line][row]="x" if ind == True else "o"
    else:
        print("Cell already marked. Make another turn!")
        make_move(gametable)
    return gametable
    

#Formatting and printing the gametable    
def print_play_table(gametable):
    print ("{:<3} {:<3} {:<3} {:<3}".format("","0","1","2"))
    for k, v in gametable.items():
        a, b, c = v
        print ("{:<3} {:<3} {:<3} {:<3}".format(k, a, b, c))
    
#Checking if the game is over and with what results 
def check_winner (gametable):
    for line in range(3):
        #Checking lines
        if len(set(gametable[line]))==1 and "-"not in gametable[line]:
            return gametable[line][0]
        #Checking rows
        if (len(set([gametable[i][line] for i in range(3)]))==1 and
                not gametable[0][line]=="-"):
            return gametable[0][line]
    #Checking positive diagonal
    if (len(set([gametable[i][i] for i in range(3)]))==1 and
            not gametable[1][1]=="-"):
        return gametable[1][1]
    #Checking negative diagonal
    if (len(set([gametable[i][2-i] for i in range(3)]))==1 and
            not gametable[1][1]=="-"):
        return gametable[1][1]
    #Checking for the draw
    if not "-" in "".join(list(map("".join,
                                   [gametable[i] for i in range(3)]))):
        return "draw"
    pass

#Main game function with game loop and recursion to play again
def play_game():
    game_table = {k:["-","-","-"]for k in range(3)}
    print_play_table(game_table)
    global ind 
    
    while not check_winner(game_table):
        if ind:
             print("X turn")
             game_table=make_move(game_table)
        else: 
             print("O turn")
             game_table=make_move(game_table)
        ind=not ind
        print_play_table(game_table)
        
    if check_winner(game_table) == "draw":
        print("It's a Draw!")
    else:
        print(f"{check_winner(game_table).upper()} wins!")
    if input("Play Again? Y/N:").upper()=="Y":
        ind=True
        play_game()
    else: 
        print ("Thank you for playing!")
        
        
play_game()

