# def find_max_num(array):
#     result = -1
#     for i in range(len(array)):
#         if(array[i] > result):
#             result = array[i]
#     return result


def find_max_num(array):
    result = -1
    for i in array:
        if i > result:
            result = i
    return result


print("정답 = 6 / 현재 풀이 값 = ", find_max_num([3, 5, 6, 1, 2, 4]))
print("정답 = 6 / 현재 풀이 값 = ", find_max_num([6, 6, 6]))
print("정답 = 1888 / 현재 풀이 값 = ", find_max_num([6, 9, 2, 7, 1888]))

