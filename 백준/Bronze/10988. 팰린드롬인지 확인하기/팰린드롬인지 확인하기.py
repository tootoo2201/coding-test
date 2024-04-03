def isPalindrome(strs):
    return strs == strs[::-1]

strs = input()
if isPalindrome(strs):
    print('1')
else:
    print('0')