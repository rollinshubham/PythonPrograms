import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '10_sum_of_digits.py'))
spec = importlib.util.spec_from_file_location("10_sum_of_digits", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_21](start_span)[span_21](end_span)
    assert module.sum_of_digits(123) == 6
    assert module.sum_of_digits(904) == 13
    assert module.sum_of_digits(-45) == 9
    assert module.sum_of_digits(0) == 0
    
    # Required expected output[span_22](start_span)[span_22](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()