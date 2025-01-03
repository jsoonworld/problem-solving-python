top_heights = [6, 9, 5, 7, 4]


def get_receiver_top_orders(heights):
    # 인덱스는 1부터 시작
    # 해당 탑에서 왼쪽으로 이동하면서 본인의 탑보다 크면 max 타워를 갱신
    # max 타워의 인덱스를 본인 타워 인덱스 배열에 넣기

    result = []

    for i in range(len(heights) -1, 0, -1):  # [문제점 1] 범위 문제: i는 0부터 시작해야 마지막 탑도 처리 가능.
        my_height = heights[i]
        for j in range(i):  # [문제점 2] 내부 루프가 잘못됨: j는 0부터 i-1까지 순회해야 올바르게 비교 가능.
            highest_index = i  # [문제점 3] highest_index를 반복마다 초기화하면 마지막 비교 결과만 저장됨.
            highest = my_height
            if highest > heights[j]:  # [문제점 4] 비교 조건이 잘못됨: 높이가 더 작으면 갱신이 이루어져야 함.
                highest_index = j
        result.append(j+1)  # [문제점 5] j+1을 추가하면 마지막 비교한 j의 값이 잘못 결과로 반영됨.

    return result.reverse()  # [문제점 6] reverse()는 None을 반환하므로 결과가 출력되지 않음.
    





print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ",get_receiver_top_orders([6,9,5,7,4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ",get_receiver_top_orders([3,9,9,3,5,7,2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ",get_receiver_top_orders([1,5,3,6,7,6,5]))