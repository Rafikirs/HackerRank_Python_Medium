# Exercise: No Idea!
# URL: https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true
# Description: Count your happiness based on how many array elements belong to your liked set (+1) or disliked set (–1)

ar_length, set_length = map(int, input().split())

ar = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

happiness = 0

for n in ar:
    if n in A:
        happiness += 1
    if n in B:
        happiness -= 1
        
print(happiness)
