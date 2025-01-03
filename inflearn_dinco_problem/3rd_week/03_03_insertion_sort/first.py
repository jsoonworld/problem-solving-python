input = [4, 6, 2, 9, 1]


# def insertion_sort(array):
#     # 앞부분을 정렬 시키고, 뒤에 값으로 확장하면 앞에 있는 값들을 모두 정렬상태로 변경
#     n = len(array)
#     end_index = 1
#     while end_index <= n:  # [문제점 1] 범위 오류: `end_index`가 `n`과 같아질 때 `array[end_index]`는 IndexError 발생 가능.
#         for i in range(end_index):  # [문제점 2] 내부 루프는 범위 내에서 값을 정렬하려 하지만,
#             if array[end_index] < array[i]:  # [문제점 3] `end_index`를 기준으로 비교. 루프가 끝날 때마다 중복된 스왑이 발생.
#                 array[end_index], array[i] = array[i], array[end_index]  # [문제점 4] 삽입 정렬에서는 스왑이 아니라 요소를 이동해야 함.
#         end_index += 1  # `end_index`가 `n`을 초과하면 동작이 중단되어야 함.
#
#     return  # [문제점 5] 함수가 결과를 반환하지 않음. `return array`로 수정 필요.

# def insertion_sort(array):
#     n = len(array)
#     # 앞에 있는 값을 정렬 되어 있다고 생각.
#     # 추가되는 값을 앞에 있는 값과 비교해서 정렬
#     # 만약 가장 크다면 맨 뒤에 추가를 하고
#     # 만약 작다면 비교하면서 앞으로 이동
#
#     # 외부 루프 : 두 번째 요소부터 시작
#     for i in range(1, n):
#         key = array[i] # 삽입하려는 값을 임시로 저장
#         j = i - 1 # 정렬된 부분의 마지막 인덱스
#
#         while j >= 0 and array[j] > key:
#             array[j + 1] = array[j] # 요소를 오른쪽으로 이동
#             j -= 1
#
#         array[j + 1] = key
#
#     return array

def insertion_sort(array):
    n = len(array)
    # 두 번째 요소부터 배열 끝까지 반복
    for i in range(1, n):
        key = array[i]  # 현재 삽입할 값을 임시로 저장
        j = i - 1  # 정렬된 부분의 마지막 인덱스

        # 정렬된 부분을 거꾸로 탐색하며, 삽입할 위치를 찾음
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]  # 요소를 오른쪽으로 이동
            j -= 1

        # 삽입할 위치에 값을 삽입
        array[j + 1] = key

    return array  # 정렬된 배열 반환




insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))