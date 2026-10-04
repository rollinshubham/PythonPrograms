import importlib.util

spec = importlib.util.spec_from_file_location(
    "largest", "Code/02_largest_of_three.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.largest_of_three(3, 7, 5) == 7
assert module.largest_of_three(10, 2, 4) == 10
assert module.largest_of_three(-1, -5, -3) == -1
assert module.largest_of_three(6, 6, 2) == 6

print("All test cases passed.")