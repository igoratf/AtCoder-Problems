    n = int(input())

    words = {}
    anagrams = 0

    for i in range(n):
        word = "".join(sorted(input()))
        if word not in words:
            words[word] = 1
        else:
            anagrams += words[word]
            words[word] += 1

    print(anagrams)
