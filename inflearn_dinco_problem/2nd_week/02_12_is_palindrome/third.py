input = "abcba"


def is_palindrome_first(string):
    # 재귀를 활용하려면 맨 앞과 끝을 비교하고 같으면 제거
    if string[0] == string[len(string)-1]:
        string = string[0:-1]
        is_palindrome_first(string)
    else:
        False
    return True

def is_palindrome_second(string):
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    return is_palindrome_second(string[1:-1])



print(is_palindrome_first(input))