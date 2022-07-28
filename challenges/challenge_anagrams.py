def selection_sort(list):
    length = len(list)
    for index in range(length):
        min_index = index

        for x in range(index + 1, length):
            if list[x] < list[min_index]:
                min_index = x

        list[min_index], list[index] = list[index], list[min_index]

    return list


def split(word):
    return [char for char in word]


def is_anagram(first_string: str, second_string: str):
    first_splited = split(first_string.lower())
    second_splied = split(second_string.lower())

    first = selection_sort(first_splited)
    second = selection_sort(second_splied)

    return first == second
