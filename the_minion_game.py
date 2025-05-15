# Exercise: The Minion Game
# URL: https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
# Description: This function implements The Minion Game, where two players (Kevin and Stuart) score points based on substrings of a given string.
# Kevin scores points for substrings starting with vowels.
# Stuart scores points for substrings starting with consonants.
# The function calculates each player's score and prints the winner's name with their score, or "Draw" if scores are equal.

def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            kevin_score += len(string) - i
        else:
            stuart_score += len(string) - i
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")
