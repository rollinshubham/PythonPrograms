def find_missing_number(numbers, n):
    # n is the expected length of the sequence including the missing number
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)
    return expected_sum - actual_sum