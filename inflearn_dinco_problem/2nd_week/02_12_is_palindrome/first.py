input = "abcba"


def is_palindrome(string):
    right = len(string) -1
    left = 0
    while left <= right:
        if string[left] != string[right]:
            return False
        else:
            left += 1
            right -= 1
    return True


print(is_palindrome(input))