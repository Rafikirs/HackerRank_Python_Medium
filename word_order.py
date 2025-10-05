# Exercise: Word Order
# URL: https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true
# Description: Count how many times each unique word appears, keeping their original order.

N = int(input())
word_list = []
counts = {}

for _ in range(N):
    word = input()
    word_list.append(word)
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(len(counts))
print(*[item[1] for item in counts.items()])
