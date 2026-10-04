import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '09_palindrome_number.py'))
spec = importlib.util.spec_from_file_location("09_palindrome_number", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_15](start_span)[span_15](end_span)
    assert module.is_palindrome(121) is True
    assert module.is_palindrome(123) is False
    assert module.is_palindrome(1) is True
    assert module.is_palindrome(3333) is True
    
    # Required expected output[span_16](start_span)[span_16](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()