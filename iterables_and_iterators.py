# Exercise: Iterables and Iterators
# URL: https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
# Description: Using the itertools library to calculate probabilities

from itertools import combinations

N = int(input())
letters = input().split()
k = int(input())

combis = list(combinations(letters, k))
a_count = 0

for c in combis:
    if "a" in c:
        a_count += 1

print(a_count / len(combis))
