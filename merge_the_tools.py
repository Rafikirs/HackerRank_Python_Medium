# Exercise: Merge the tools
# URL: https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true
# Description: Print substrings of a string while removing duplicated letters within each substring

def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substring = string[i:i+k]
        result = ""
        for char in substring:
            if char not in result:
                result += char
        print(result)
