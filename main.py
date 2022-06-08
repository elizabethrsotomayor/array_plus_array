def array_plus_array(arr1: list, arr2: list) -> int:
    """
    Return the sum of all the elements of two lists
    :param arr1:
    :param arr2:
    :return:
    """
    total = 0
    big_arr = arr1 + arr2
    for i in big_arr:
        total += i
    return total
