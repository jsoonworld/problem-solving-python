top_heights = [6, 9, 5, 7, 4]

def get_receiver_top_orders(heights):
    result = []  # 결과를 저장할 리스트 초기화

    # 오른쪽 끝에서부터 왼쪽으로 순회
    for i in range(len(heights) - 1, -1, -1):
        my_height = heights[i]  # 현재 탑의 높이 저장
        found = False  # 수신할 탑을 찾았는지 여부

        # 현재 탑의 왼쪽에 있는 탑들을 확인
        for j in range(i - 1, -1, -1):
            if heights[j] > my_height:  # 더 높은 탑을 찾았을 경우
                result.append(j + 1)  # 인덱스를 1부터 시작하도록 조정하여 저장
                found = True  # 찾음 여부를 True로 설정
                break  # 더 이상 탐색하지 않음

        if not found:  # 왼쪽에 더 높은 탑이 없는 경우
            result.append(0)  # 0을 결과 리스트에 추가

    # 결과 리스트는 오른쪽에서 왼쪽으로 탐색한 순서이므로 역순으로 뒤집어야 함
    result.reverse()
    return result

# 테스트 케이스 실행 및 결과 출력
print(get_receiver_top_orders(top_heights))  # [0, 0, 2, 2, 4] 가 반환되어야 한다!

print("\n정답 = [0, 0, 2, 2, 4] / 현재 풀이 값 = ", get_receiver_top_orders([6, 9, 5, 7, 4]))
print("정답 = [0, 0, 0, 3, 3, 3, 6] / 현재 풀이 값 = ", get_receiver_top_orders([3, 9, 9, 3, 5, 7, 2]))
print("정답 = [0, 0, 2, 0, 0, 5, 6] / 현재 풀이 값 = ", get_receiver_top_orders([1, 5, 3, 6, 7, 6, 5]))
