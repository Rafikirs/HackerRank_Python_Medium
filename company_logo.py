# Exercice: Company Logo
# URL: https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true
# Description: Print the three most common characters of a string along with their occurrence count

if __name__ == '__main__':
    s = input()
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    sorted_freq = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    for char, count in sorted_freq[:3]:
        print(char, count)






