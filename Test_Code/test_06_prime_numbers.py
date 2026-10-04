import importlib.util

spec = importlib.util.spec_from_file_location(
    "prime", "Code/06_prime_numbers.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(2) is True
assert module.is_prime(7) is True
assert module.is_prime(9) is False
assert module.is_prime(1) is False
assert module.is_prime(0) is False
assert module.is_prime(-5) is False

print("All test cases passed.")