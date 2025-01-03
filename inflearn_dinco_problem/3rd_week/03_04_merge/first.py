array_a = [1, 2, 3, 5]
array_b = [4, 6, 7, 8]


# def merge(array1, array2):
#     # array1의 인덱스와 array2의 인덱스를 비교해서 값이 작은 걸 새로운 배열에 추가한다.
#     # 만약 array1의 인덱스와 array2의 인덱스 위치가 반대라면 반대 배열의 값을 빈배열에 모두 추가한다.
#
#     result = []
#     left_index = 0
#     right_index = 0
#
#     # [문제점 1] `while len(result) <= len(array1) + len(array2)` 조건:
#     # - `result`의 길이를 기준으로 반복 조건을 설정하면 무한 루프가 발생할 가능성이 있음.
#     # - 대신 `left_index`와 `right_index`가 각각의 배열 끝에 도달했는지 확인해야 함.
#
#     while len(result) <= len(array1) + len(array2):
#         if array1[left_index] <= array2[right_index]:
#             result.append(array1[left_index])
#             left_index += 1
#
#             # [문제점 2] `left_index == len(array1)` 조건:
#             # - 이미 `left_index`가 배열 끝에 도달했을 때, 모든 남은 요소를 처리하려는 의도.
#             # - 그러나 내부 루프(`for`)로 인해 중복된 값이 추가될 가능성이 있음.
#             # - 반복문에서 남은 요소를 처리하려면 `extend`를 사용하는 방식이 적합.
#
#             if left_index == len(array1):
#                 for right_index in range(len(array2)):  # [문제점 3] `range(len(array2))`로 인해 중복 추가 가능.
#                     result.append(array2[right_index])
#         else:
#             result.append(array2[right_index])
#             right_index += 1
#
#             # [문제점 4] `right_index == len(array2)` 조건:
#             # - 위와 동일하게, 남은 요소를 처리하려고 하지만 중복 추가될 가능성이 있음.
#             # - 남은 요소를 처리할 때 루프 대신 슬라이싱을 활용하면 더 안전.
#
#             if right_index == len(array2):
#                 for left_index in range(len(array1)):  # [문제점 5] 중복된 인덱스로 인해 값이 잘못 추가될 수 있음.
#                     result.append(array1[left_index])
#
#     # [문제점 6] 마지막 남은 요소를 처리하는 코드가 루프 내부에서만 처리됨:
#     # - 남은 요소를 처리하는 로직을 루프 외부로 분리하여 중복 문제를 방지해야 함.
#
#     return result


def merge(array_left, array_right):
    # 두 배열을 정렬을 하면서 합친다.
    # array[1] 과 2를 비교한다. 값이 작으면 result에 추가하고 index를 키운다. 만약 키운 index가 len(array)보다 크면 반대 array를 extend해서 결과에 모두 붙인다.
    result = []
    left_index = 0
    right_index = 0

    while left_index != len(array_left) and right_index != len(array_right):

        if array_left[left_index] < array_right[right_index]:
            result.append(array_left[left_index])
            left_index += 1
            if left_index == len(array_left):
                result.extend(
                    array_right[right_index:])  # [문제점 1] 이 조건문은 루프 외부에서 처리하는 것이 더 적합. 루프 내부에서 처리 시 중복 조건 평가 가능성.
        else:
            result.append(array_right[
                              array_right])  # [문제점 2] 잘못된 배열 접근. array_right[array_right]는 의미 없는 참조. array_right[right_index]로 수정 필요.
            right_index += 1
            if right_index == len(array_right):
                result.extend(array_left[
                              left_index:])  # [문제점 3] 이 조건문도 루프 외부에서 처리하는 것이 더 적합. 남은 요소를 처리하는 코드는 반복문 외부에서 처리하는 것이 더 효율적.

    return result


print(merge(array_a, array_b))  # [1, 2, 3, 4, 5, 6, 7, 8] 가 되어야 합니다!

print("정답 = [-7, -1, 5, 6, 9, 10, 11, 40] / 현재 풀이 값 = ", merge([-7, -1, 9, 40], [5, 6, 10, 11]))
print("정답 = [-1, 2, 3, 5, 10, 40, 78, 100] / 현재 풀이 값 = ", merge([-1, 2, 3, 5, 40], [10, 78, 100]))
print("정답 = [-1, -1, 0, 1, 6, 9, 10] / 현재 풀이 값 = ", merge([-1, -1, 0], [1, 6, 9, 10]))
