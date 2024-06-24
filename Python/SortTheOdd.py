def sort_array(source_array):
    odd_array = iter(sorted([x for x in source_array if x % 2 != 0]))
    return [next(odd_array) if x % 2 != 0 else x for x in source_array]

print(sort_array([3, 9, 2, 0, 1]))

