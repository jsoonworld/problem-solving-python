def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zero_group_count = 0
    one_group_count = 0

    if string[0] == '0':
        zero_group_count += 1
    else:
        one_group_count += 1

    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            if string[i] == '0':
                zero_group_count += 1
            else:
                one_group_count += 1
    return min(zero_group_count, one_group_count)

input = "011110"
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)