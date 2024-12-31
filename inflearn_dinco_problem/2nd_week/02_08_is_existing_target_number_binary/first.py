finding_target = 14
finding_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def index_of_array_half(array):
    return len(array)//2


def is_existing_target_number_binary(target, array):
    while len(array) > 0:
        middle_index = index_of_array_half(array)
        middle_value = array[middle_index]

        if target == middle_value:
            return True
        elif target > middle_value:
            array = array[middle_index +1:]
        else:
            array = array[:middle_index]

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)