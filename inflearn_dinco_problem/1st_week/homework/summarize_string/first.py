def summarize_string(input_str):
    # acccdeee
    # 알파벳이 달라지는 순간
    # append_alpha 담아둔다.
    # count +1
    # 다음 문자와 비교해서 달라지는 순간
    # appned_alpha와 count를 result 에 appned한다.
    # append_alpha에 달라진 문자를 저장하고
    # count = 1로 초기화 한다.

    result = ""
    count = 1
    append_alpha = input_str[0]
    for i in range(1,len(input_str)):
        if input_str[i] != append_alpha:
            result += append_alpha
            result += str(count)
            result += "/"
            append_alpha = input_str[i]
            count = 1
        else:
            count += 1
    else:
        result += append_alpha
        result += str(count)


    return result


input_str = "acccdeee"

print(summarize_string(input_str))

