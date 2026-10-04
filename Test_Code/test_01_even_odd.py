import importlib.util

spec = importlib.util.spec_from_file_location(
    "even_odd", "Code/01_even_odd.py"
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.even_or_odd(2) == "Even"
assert module.even_or_odd(7) == "Odd"
assert module.even_or_odd(0) == "Even"
assert module.even_or_odd(-4) == "Even"

print("All test cases passed.")