input = [4, 6, 2, 9, 1]


def selection_sort(array):
    n = len(array)

    for i in range(n - 1):  # i번째 위치에 올바른 값을 찾기 위한 반복.
        min_index = i  # i번째 값을 현재 최소값의 위치로 설정.

        for j in range(i + 1, n):  # i+1부터 끝까지 최솟값의 위치를 찾음.
            if array[min_index] > array[j]:  # 현재 최소값보다 더 작은 값을 발견하면,
                min_index = j  # 해당 위치를 최솟값의 위치로 갱신.

        # i번째 값과 최솟값 위치를 교환.
        array[i], array[min_index] = array[min_index], array[i]

    return array


# 테스트 실행
print("정답 = [1, 2, 4, 6, 9] / 현재 풀이 값 = ", selection_sort([4, 6, 2, 9, 1]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ", selection_sort([3, -1, 17, 9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ", selection_sort([100, 56, -3, 32, 44]))
