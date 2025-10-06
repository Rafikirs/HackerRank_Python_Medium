# Exercise: Athlete Sort
# URL: http://hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true
# Description: Sorting lists based on a given index

if __name__ == '__main__':
    n, m = map(int, input().split())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    arr = sorted(arr, key=lambda x: x[k])
    
    for student in arr:
        print(*student)
