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






