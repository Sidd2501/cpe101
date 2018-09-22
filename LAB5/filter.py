def are_positive(input_list):
    output_list = []
    for i in range(0,len(input_list)):
        if input_list[i] > 0:
            output_list.append(input_list[i])
    return output_list


def are_greater_than_n(input_list, n):
    output_list = []
    i = 0
    while i < len(input_list):
        if input_list[i] > n:
            output_list.append(input_list[i])
        i += 1
    return output_list


def are_divisible_by_n(input_list, n):
    return [input_list[i] for i in range(0, len(input_list)) if input_list[i] % n == 0]
