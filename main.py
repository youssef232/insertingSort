"""
    insertion sort: both ascent and descent


"""


def insertion_sort_ascent(arr):
    for current_position in range(1, len(arr)):
        key = arr[current_position]
        previous_index = current_position - 1
        while arr[previous_index] > key and previous_index >= 0:
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1
        arr[previous_index + 1] = key
    return arr


def insertion_sort_descent(arr):
    """

    :param arr: set of numbers like [32, 42, 21, 1, 23, 44, 6]
    :return: ordered array
    [32 , 42, 21, 1 , 23, 44, 6]
      |    |
      |     current_position
      previous index
    """
    for index in range(1, len(arr)):
        key = arr[index]
        previous_index = index - 1
        while key > arr[previous_index] and previous_index >= 0:
            arr[previous_index + 1] = arr[previous_index]
            previous_index -= 1
        arr[previous_index + 1] = key
    return arr


array = [24, 53, 22, 11, 2, 3, 4]
print("array sorted in ascent = ",  format(insertion_sort_ascent(array)))
print("array sorted in descent = ",  format(insertion_sort_descent(array)))
