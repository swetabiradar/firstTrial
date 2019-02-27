#!/usr/bin/env python

""" On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move. """

class Solution:

      def __init__(self,board):
          self._board = board

      def numRookCaptures(self):
          """ returns count of pawns available to capture for Rook"""

          capture_count = 0
      
          # Calulating Dimension of Rook 'R'
          for c,row in enumerate(self._board):
              for elem in row:
                  if elem == 'R':
                     R_pos = [c,row.index(elem)]
                     break
      
          # R_pos[0] = row number of 'R'
          # R_pos[1] = position of R in that row

          # we are trying iterate top,bottom and left, right boxes of R
      


          # Checking if pawn is present in left hand side or right hand side of R 

          r = self._board[R_pos[0]] #row_number of R
   
          # To the left of R
          for x in range(R_pos[1]-1,-1,-1):  #for eg: R_pos[1] = 2, we'll be iterating backwards like 1,0; -1 at the end indicates backward iteration 

              if r[x] == 'p':
                 capture_count += 1
                 break
              elif r[x] == 'B':
                 break
              else:
                 continue


          # To the right of R
          for x in range(R_pos[1]+1,8,1):  #for eg: R_pos[1] = 2, we'll be iterating backwards like 1,0; -1 at the end indicates backward iteration 

              if r[x] == 'p':
                 capture_count += 1
                 break
              elif r[x] == 'B':
                 break
              else:
                 continue
 

          # Checkig=ng if pawn is present in Top and Bottom rows of R

          # Top of R

          for row_num in range(R_pos[0]-1,-1,-1):  #for eg: R_pos[0] = 2, we'll be iterating backwards like 1,0; -1 at the end indicates backward iteration

              if self._board[row_num][R_pos[1]] == 'p':
                 capture_count += 1
                 break
              elif self._board[row_num][R_pos[1]] == 'B':
                 break
              else:
                 continue

          # Bottom of R

          for row_num in range(R_pos[0]+1,8,1):  

              if self._board[row_num][R_pos[1]] == 'p':
                 capture_count += 1
                 break
              elif self._board[row_num][R_pos[1]] == 'B':
                 break
              else:
                 continue

          return capture_count


def main():
   board = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
   board_1 = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]

   A = Solution(board_1)
   
   print('output = {}'.format(A.numRookCaptures()))

if __name__ == '__main__':
  main()
