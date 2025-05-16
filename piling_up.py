# Exercice: Piling Up!
# URL: https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true
# Description: This program checks if it's possible to stack a series of cubes into a vertical pile 
# where each cube is equal to or smaller than the cube directly beneath it.

def can_stack_cubes(blocks):
    left, right = 0, len(blocks) - 1
    last_block = float('inf')  
    
    while left <= right:
        if blocks[left] >= blocks[right]:
            if blocks[left] <= last_block:
                last_block = blocks[left]
                left += 1
            else:
                return "No"
        else:
            if blocks[right] <= last_block:
                last_block = blocks[right]
                right -= 1
            else:
                return "No"
    return "Yes"
