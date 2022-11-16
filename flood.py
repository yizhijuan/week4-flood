from typing import List
import sys
sys.setrecursionlimit(50000)

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    """Returns board with old values replaced with new values through flood filling starting from the coordinates x, y
    Args:
        input_board (List[str])
        old (str): Value to be replaced
        new (str): Value that replaces the old
        x (int): X-coordinate of the flood start point
        y (int): Y-coordinate of the flood start point
    Returns:
        List[str]: Modified board
    """
    if input_board[x][y] == old:
        if y == len(board[0]):
            input_board[x] = input_board[x][:y] + new
        else:
            input_board[x] = input_board[x][:y] + new + input_board[x][y+1:]
        if x >= 1 and x <= len(board)-1 and y >= 0 and y <= len(board[0])-1:
            flood_fill(input_board=input_board, old=old, new=new, x=x-1, y=y)
        if x >= 0 and x <= len(board)-1 and y >= 0 and y <= len(board[0]) - 2:
            flood_fill(input_board=input_board, old=old, new=new, x=x, y=y+1)      
        if x >= 0 and x <= len(board)-1 and y >= 1 and y <= len(board[0])-1:   
            flood_fill(input_board=input_board, old=old, new=new, x=x, y=y-1)
        if x >= 0 and x <= len(board)-2 and y >= 0 and y <= len(board[0])-1:    
            flood_fill(input_board=input_board, old=old, new=new, x=x+1, y=y)
    return input_board

# modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)
modified_board = flood_fill(input_board=board, old=".", new="~", x=0, y=0)

for a in modified_board:
    print(a)
