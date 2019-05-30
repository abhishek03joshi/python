#!/bin/python
from random import randint

board = []

for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)
ship_row = []
ship_col = []
for r in range(3):
  ship_row.append(random_row(board))
for c in range(3):
  ship_col.append(random_col(board))

print ship_row
print ship_col
correct_guesses = 0
for turn in range(4):

  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))
  

  if (guess_row == ship_row[0] and guess_col == ship_col[0]) or (guess_row == ship_row[1] and guess_col == ship_col[1]) or (guess_row == ship_row[2] and guess_col == ship_col[2]) :
    print "Congratulations! You sunk my battleship!"
    correct_guesses += 1
    if correct_guesses > 2:
      exit(0)
  
  else:
    if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
      if turn == 3:
        print "Game Over"

    print "Turn", turn+1   
