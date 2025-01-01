
input = "7 3"
def josephus_problem(n, k):
    array = list(range(1, n+1))
    result = []
    target_index = 0

    while array:
        target_index = (target_index + k - 1) % len(array)
        result.append(array.pop(target_index))
    return f"<{', '.join(map(str, result))}>"

n, k = map(int, input.split())
print(josephus_problem(n, k))
