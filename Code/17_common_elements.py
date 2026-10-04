def find_common_elements(list1, list2):
    # Using list comprehension to maintain order, though sets are faster
    return [item for item in list1 if item in list2]