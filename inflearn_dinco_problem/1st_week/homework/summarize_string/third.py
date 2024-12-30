# def summarize_string(input_str):
#     result = []
#     count = 1
#     append_alpha = input_str[0]
#
#     for i in range(1, len(input_str)):
#         if input_str[i] != append_alpha:
#             result.append(append_alpha + str(count))
#             append_alpha = input_str[i]
#             count = 1
#         else:
#             count += 1
#     result.append(append_alpha + str(count))
#     return "/".join(result)

def summarize_string(input_str):
    result = []
    count = 1
    append_alpha = input_str[0]

    for i in range(1, len(input_str)):
        if input_str[i] != append_alpha:
            result.append(append_alpha + str(count))
            append_alpha = input_str[i]
            count = 1
        else:
            count += 1
    result.append(append_alpha + str(count))
    return "/".join(result)


input_str = "acccdeee"
print(summarize_string(input_str))