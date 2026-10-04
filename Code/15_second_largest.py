def find_second_largest(numbers):
    unique_nums = list(set(numbers))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort(reverse=True)
    return unique_nums[1]