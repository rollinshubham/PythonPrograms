def reverse_number(n):
    sign = -1 if n < 0 else 1
    n = abs(n)
    reversed_n = int(str(n)[::-1])
    return sign * reversed_n