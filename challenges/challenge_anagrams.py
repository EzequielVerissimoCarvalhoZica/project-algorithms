def selection_sort(input_list):
    length = len(input_list)
    for index in range(length):
        min_index = index

        for x in range(index + 1, length):
            if input_list[x] < input_list[min_index]:
                min_index = x

        input_list[min_index], input_list[index] = input_list[index], input_list[min_index]

    return input_list


def split(word):
    return [char for char in word]


def is_anagram(first_string: str, second_string: str):
    first_splited = split(first_string.lower())
    second_splied = split(second_string.lower())

    first = selection_sort(first_splited)
    second = selection_sort(second_splied)

    return first == second

is_anagram("acd", "xca")