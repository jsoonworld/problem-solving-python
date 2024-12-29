input = "011110"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_count = 0
    one_count = 0

    # 전체 0과 1의 개수를 계산
    for num in string:
        if num == '0':  # 문자 '0'을 비교하는 조건은 맞음
            zero_count += 1
        else:
            one_count += 1
    # 위 부분은 전체 0과 1의 개수를 정확히 세기 때문에 문제가 없습니다.

    less_number_count = 0
    less_number = ''
    if zero_count >= one_count:
        less_number = '1'
        less_number_count = one_count  # 맞음: 더 적게 등장한 개수는 one_count.
    else:
        less_number = '0'
        less_number_count = zero_count  # 맞음: 더 적게 등장한 개수는 zero_count.

    # 개선 방향:
    # less_number와 less_number_count는 올바르게 설정되었음.
    # 하지만 이 변수들은 "연속된 그룹의 개수"를 계산할 때 의미가 약해질 수 있으므로
    # 연속된 그룹의 개수를 별도로 계산하는 것이 더 적합합니다.

    count = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:  # 연속된 숫자를 찾는 조건은 맞음
            if string[i] == less_number:  # 틀림: less_number는 문자로 저장되어 있지만, 이 비교의 의도는 그룹 단위로 판단하는 것이므로 부적절.
                count += 1
    # 개선 방향:
    # string[i]와 less_number를 비교하는 것은 문제 없음.
    # 하지만 연속된 그룹의 개수는 그룹 단위로 계산해야 하며, 단순히 less_number와 비교하는 것으로는 충분하지 않습니다.

    result = less_number_count - count  # 틀림: less_number_count는 전체 개수, count는 연속된 그룹 수를 기반으로 계산되어야 함.
    # 개선 방향:
    # result를 less_number_count와 count를 사용해 계산하는 것이 아니라,
    # "전체 연속된 그룹 중 뒤집을 그룹 수"를 기반으로 계산해야 합니다.

    return result


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

# 개선 방향 요약:
# 1. 연속된 그룹의 개수를 정확히 세는 별도의 로직 추가.
# 2. less_number_count를 그룹 단위로 계산하도록 수정.
# 3. 최종 결과는 전체 그룹의 개수를 기반으로 계산 (예: 더 적은 그룹을 뒤집음).
