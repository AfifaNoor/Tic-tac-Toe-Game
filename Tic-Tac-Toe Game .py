#!/usr/bin/env python
# coding: utf-8

# In[ ]:


player1=input("Enter your name: ")
player2=input("Enter your name: ")

print(f'Welcome {player1} and {player2} to Tic-Tac-Toe Game.')

instructions="""
This is your Tic-Tac-Toe Game Board.

  1  |  2  |  3  
-----|-----|-----
  4  |  5  |  6
-----|-----|-----    
  7  |  8  |  9

Instructions:
1.Enter number between (1-9) according to the position of every box.
2.You must fill all the box of the board.
3.Player 1 will go first as an X."""




print(instructions)


board=['-','-','-','-','-','-','-','-','-']


def display_board():
    print(f"{board[0]} + | +{board[1]} + | + {board[2]}")
    print("----|----|----")
    print(f"{board[3]} + | +{board[4]} + | + {board[5]}")
    print("----|----|----")
    print(f"{board[6]} + | +{board[7]} + | + {board[8]}")

def check_win(board):
    player1='X'
    player2='O'
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    if player1 == win:
        print("Player1 Won.")
    elif player2==win:
        print( "Player2 Won.")
    else:
        print("Draw.")
display_board()



    
    
    


# In[ ]:




