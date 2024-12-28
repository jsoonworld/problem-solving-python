def find_max_occurred_alphabet(string):

    occurrence_alphabet_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        occurrence_alphabet_array[arr_index] += 1

    max_occurrence = 0
    max_alphabet_index = 0
    for index in range(len(occurrence_alphabet_array)):
        alphabet_occurrence = occurrence_alphabet_array[index]
        if alphabet_occurrence > max_occurrence:
            max_occurrence = alphabet_occurrence
            max_alphabet_index = index

    return chr(max_alphabet_index + ord('a'))



result = find_max_occurred_alphabet
print("정답 = i 현재 풀이 값 =", result("hello my name is dingcodingco"))
print("정답 = e 현재 풀이 값 =", result("we love algorithm"))
print("정답 = b 현재 풀이 값 =", result("best of best youtube"))



# 설계

# string 의 값을 입력 받는다 'abc'
# 0으로 초기화되어있는 배열을 만든다 크기는 26 (알파벳의 크기)
# a - > ord(a) = 97
# ord(a - ord('a) ) = 0
# 이렇게 해서 배열에 값을 저장
# 배열을 순회하면서 맥스 크기의 배열의 인덱스를 출력한다
# 인덱스가 8이면 이 값을 다시 알파벳으로 만들어야 한다.
# chr() 이 함수는 숫자를 문자로 만들어주는 것
# chr(97) = a 가 나옴
# chr(index + ord('a) ) = index의 영어가 나옴 = result