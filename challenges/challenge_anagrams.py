# def merge_sort(list):
#     if len(list) <= 1:
#         return list

#     mid = len(list) // 2
#     left, right = merge_sort(list[:mid]), merge_sort(list[mid:])

#     return merge(left, right, list.copy())


# def merge(left, right, merged):
#     left_side, right_side = 0, 0

#     while left_side < len(left) and right_side < len(right):
#         if left[left_side] <= right[right_side]:
#             merged[left_side + right_side] = left[left_side]
#             left_side += 1
#         else:
#             merged[left_side + right_side] = right[right_side]
#             right_side += 1

#     for left_side in range(left_side, len(left)):
#         merged[left_side + right_side] = left[left_side]

#     for right_side in range(right_side, len(right)):
#         merged[left_side + right_side] = right[right_side]

#     return merged

def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end

    while True:
        while low <= high and array[high] >= pivot:
            high = high - 1

        while low <= high and array[low] <= pivot:
            low = low + 1

        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break

    array[start], array[high] = array[high], array[start]

    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def split(word):
    return [char for char in word]


def is_anagram(first_string: str, second_string: str):
    if first_string == "" or second_string == "":
        return False

    first_splited = split(first_string.lower())
    second_splied = split(second_string.lower())

    quick_sort(first_splited, 0, len(first_splited) - 1)
    quick_sort(second_splied, 0, len(first_splited) - 1)

    return first_splited == second_splied
