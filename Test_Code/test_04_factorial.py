import importlib.util

spec = importlib.util.spec_from_file_location(
    "factorial", "Code/04_factorial.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.factorial(0) == 1
assert module.factorial(1) == 1
assert module.factorial(5) == 120
assert module.factorial(6) == 720

try:
    module.factorial(-1)
    assert False, "Expected ValueError for negative input"
except ValueError:
    pass

print("All test cases passed.")