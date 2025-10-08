# Exercise: Regex Substitution
# URL: https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true
# Description: Using re.sub()

import re

n = int(input())
for _ in range(n):
    line = input()
    line = re.sub(r'(?<= )&&(?= )', 'and', line)
    line = re.sub(r'(?<= )\|\|(?= )', 'or', line)
    print(line)
