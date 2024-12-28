def find_max_plus_or_multiply(array):
    plus_or_multiply_sum = 0
    for number in array:
        if number <= 1 or plus_or_multiply_sum <= 1:
            plus_or_multiply_sum += number
        else:
            plus_or_multiply_sum *= number
    return plus_or_multiply_sum


result = find_max_plus_or_multiply
print("정답 = 728 현재 풀이 값 =", result([0,3,5,6,1,2,4]))
print("정답 = 8820 현재 풀이 값 =", result([3,2,1,5,9,7,4]))
print("정답 = 270 현재 풀이 값 =", result([1,1,1,3,3,2,5]))


# 숫자 사이제 + 혹은 x 연산자를 넣어 결과정으로 가장 큰 수를 구하는 프로그램
# 숫자가 3개면 1, 2, 3
# x가 2개이고 + 가 0개 -> 위치는 1 x 2 x 3,
# x가 1개이고 + 가 1개 -> 1 x 2 + 3, 1 + 2 x 3
# x가 0개이고 + 가 2개