def square_all(input_list):
    output_list = input_list
    for i in range(0,len(input_list)):
        output_list[i] = input_list[i] * input_list[i]
    return output_list


def add_n_all(input_list, n):
    output_list = input_list
    i = 0
    while i < len(input_list):
        output_list[i] = input_list[i] + n
        i += 1
    return output_list


def even_or_odd_all(input_list):
    return [input_list[i] % 2 != 1 for i in range(0,len(input_list))]
