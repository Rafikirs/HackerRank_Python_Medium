# Exercise: Compress the String!
# URL: https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true
# Description: Compressing consecutive identical characters in a string and output their counts

num_list = list(map(int, input()))
counts = []
count = 1

for i, num in enumerate(num_list):
    if i != len(num_list) - 1:
        if num_list[i+1] != num:
            counts.append((count, num))
            count = 1
        else:
            count += 1
    else:
        counts.append((count, num))

print(*counts)
