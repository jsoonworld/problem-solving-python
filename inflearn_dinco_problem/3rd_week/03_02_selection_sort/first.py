input = [4, 6, 2, 9, 1]


# def selection_sort(array):
#     n = len(array)
#
#     # i 번째 값을 가지고 전체를  i+1부터 n번째 까지 비교를 한다.
#     # 만약 뒤에있는 값중에 i번째 값보다 작은 값이 있다면 i번째와 스왑한다.
#     for i in range(n-1):  # 전체 배열에서 i 번째 위치를 기준으로 반복.
#         min = array[i]  # [문제점 1] 'min' 변수는 단순히 값을 복사. 위치 정보는 없음.
#         for j in range(n-i):  # [문제점 2] 내부 루프 범위가 잘못됨. 항상 0부터 비교를 시작함.
#             if min > array[j]:  # i 이후의 값들을 비교해야 하지만, 잘못된 범위로 인해 불필요한 비교 발생.
#                 min, array[j] = array[j], min  # [문제점 3] 'min'과 'array[j]'를 단순히 스왑. 배열에 제대로 반영되지 않음.

# # 제일 작은 값을 찾아서 맨 앞으로
# def selection_sort(array):
#     n = len(array)
#     for i in range(n-1):
#         min_index = i  # 현재 최소값의 인덱스를 저장
#         for j in range(min_index+1, n):  # [문제 1] min_index+1 대신 i+1이어야 함
#             if array[min_index] > array[j]:
#                 # [문제 2] 최솟값을 찾았을 때 값을 즉시 스왑하면 선택 정렬의 원칙에 어긋남.
#                 # 내부 반복문이 끝난 후 한 번만 스왑해야 함.
#                 array[min_index], array[j] = array[j], array[min_index]
#     return array


# 제일 작은 값을 찾아서 맨 앞으로
def selection_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i  # 현재 최소값의 인덱스를 저장
        for j in range(i+1, n):  # [문제 1] min_
            if array[min_index] > array[j]:
                min_index = j
        array[min_index], array[i] = array[i], array[min_index]
    return array

selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ",selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",selection_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",selection_sort([100,56,-3,32,44]))