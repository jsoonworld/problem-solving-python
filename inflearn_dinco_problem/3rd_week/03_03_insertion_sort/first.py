input = [4, 6, 2, 9, 1]


def insertion_sort(array):
    # 앞부분을 정렬 시키고, 뒤에 값으로 확장하면 앞에 있는 값들을 모두 정렬상태로 변경
    n = len(array)
    end_index = 1
    while end_index <= n:  # [문제점 1] 범위 오류: `end_index`가 `n`과 같아질 때 `array[end_index]`는 IndexError 발생 가능.
        for i in range(end_index):  # [문제점 2] 내부 루프는 범위 내에서 값을 정렬하려 하지만,
            if array[end_index] < array[i]:  # [문제점 3] `end_index`를 기준으로 비교. 루프가 끝날 때마다 중복된 스왑이 발생.
                array[end_index], array[i] = array[i], array[end_index]  # [문제점 4] 삽입 정렬에서는 스왑이 아니라 요소를 이동해야 함.
        end_index += 1  # `end_index`가 `n`을 초과하면 동작이 중단되어야 함.

    return  # [문제점 5] 함수가 결과를 반환하지 않음. `return array`로 수정 필요.


insertion_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!

print("정답 = [4, 5, 7, 7, 8] / 현재 풀이 값 = ",insertion_sort([5,8,4,7,7]))
print("정답 = [-1, 3, 9, 17] / 현재 풀이 값 = ",insertion_sort([3,-1,17,9]))
print("정답 = [-3, 32, 44, 56, 100] / 현재 풀이 값 = ",insertion_sort([100,56,-3,32,44]))