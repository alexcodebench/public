#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'queensAttack' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n -- board size
#  2. INTEGER k
#  3. INTEGER r_q
#  4. INTEGER c_q
#  5. 2D_INTEGER_ARRAY obstacles
#

def queensAttack(n, k, r_q, c_q, obstacles):
    # Write your code here
    if n <= 1 or k >= n**2 - 1:
        return 0
    
    if c_q > n or r_q > n or c_q < 1 or r_q < 1:
        return 0
    
    # group obstacles by relative direction to the Queen. 
    # only stores the max count of blocked positions in that group
    blocked_max = {
        'N': 0,
        'NE': 0,
        'E': 0,
        'SE': 0,
        'S': 0,
        'SW': 0,
        'W': 0,
        'NW':0        
        }
        
    def group_obstacles(r, c):
        # obstacle out of board
        if r > n or c > n:
            return
        
        # obstacle wants to sit on the Queen's spot
        if r == r_q and c == c_q:
            return
        
        # West
        if r == r_q and c < c_q:
            blocked_max['W'] = max(blocked_max['W'], c)
        # East
        elif r == r_q and c > c_q:
            blocked_max['E'] = max(blocked_max['E'], (n - c) + 1)
        # South
        elif c == c_q and r < r_q:
            blocked_max['S'] = max(blocked_max['S'], r)
        # North
        elif c == c_q and r > r_q:
            blocked_max['N'] = max(blocked_max['N'], (n - r) + 1)
        
        # After passing this, the obstacle will be in either / or \ path
        elif (r - r_q)/(c - c_q) not in [1, -1]:
            return
        # \_ NW
        elif r > r_q and c < c_q:
            blocked_max['NW'] = max(blocked_max['NW'], min(c, n - r + 1))
        # -\ SE
        elif r < r_q and c > c_q:
            blocked_max['SE'] = max(blocked_max['SE'], min(r, n - c + 1))
        # _/ NE
        elif r > r_q and c > c_q:
            blocked_max['NE'] = max(blocked_max['NE'], min(n - r + 1, n - c + 1))
        # /- SW
        elif r < r_q and c < c_q:
            blocked_max['SW'] = max(blocked_max['SW'], min(r, c))
    
        
    def sum_controled_by_queen():
        n_row = n - 1
        n_col = n - 1        
        # \
        n_left_down = min(c_q -1 , n - r_q) + min(r_q - 1, n - c_q)
        # /
        n_right_up = min(r_q - 1, c_q - 1) + min(n - r_q, n - c_q)
        
        # print(n_row + n_col + n_left_down + n_right_up)
        return n_row + n_col + n_left_down + n_right_up
    
       
    if k == 0:
        return sum_controled_by_queen()
    
    for o in obstacles:
        group_obstacles(o[0], o[1])
    
    blocked_sum = sum(val for val in blocked_max.values())
    
    return sum_controled_by_queen() - blocked_sum

    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
