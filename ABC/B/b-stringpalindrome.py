s = input()
length = len(s)

def solve(word, length):

    first = (length-1) // 2
    last = (length+3) // 2
    
    if isPalindrome(word) and isPalindrome(s[:first]) and isPalindrome(s[last-1:]):
        print("Yes")
    else:
        print("No")

def isPalindrome(word):
    palindrome = True
    size = len(word)
    start = 0
    end = size - 1

    while start <= end:
        if word[start] != word[end]:
            palindrome = False
            return palindrome
        
        start += 1
        end -= 1
    
    return palindrome

solve(s, length)
isPalindrome("ccxmm")