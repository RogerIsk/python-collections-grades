# Task - Swap list elements. Implement a method (or function) `swap` that takes the list and the two indizes as arguments,
# swap the values at the given indizes and returns the list.

def swap(lst, index1, index3):
    lst[index1], lst[index3] = lst[index3], lst[index1]
    return lst

swap_list = [23, 65, 19, 90]
swap_list = swap(swap_list, 1, 3)