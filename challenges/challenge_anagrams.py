def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left, right = merge_sort(list[:mid]), merge_sort(list[mid:])

    return merge(left, right, list.copy())


def merge(left, right, merged):
    left_side, right_side = 0, 0

    while left_side < len(left) and right_side < len(right):
        if left[left_side] <= right[right_side]:
            merged[left_side + right_side] = left[left_side]
            left_side += 1
        else:
            merged[left_side + right_side] = right[right_side]
            right_side += 1

    for left_side in range(left_side, len(left)):
        merged[left_side + right_side] = left[left_side]

    for right_side in range(right_side, len(right)):
        merged[left_side + right_side] = right[right_side]

    return merged


def split(word):
    return [char for char in word]


def is_anagram(first_string: str, second_string: str):
    first_splited = split(first_string.lower())
    second_splied = split(second_string.lower())

    first = "".join(merge_sort(first_splited))
    second = "".join(merge_sort(second_splied))

    return first == second
