# Task. You are given two lists with an unknown amount of elements. Both of those lists may have some elements in common. 
# Implement a method `intersection` that takes those two lists as arguments and returns a third list only with the elements they have in common.

list_1 = [15, 9, 10, 56, 23, 78, 5, 4, 9]
list_2 = [9, 4, 5, 36, 47, 26, 10, 45, 87]

def intersection(list_1, list_2): 
    return list(set(list_1) & set(list_2)) 

print(intersection(list_1, list_2)) # [9, 10, 4, 5]