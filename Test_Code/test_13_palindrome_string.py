import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '13_palindrome_string.py'))
spec = importlib.util.spec_from_file_location("13_palindrome_string", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_15](start_span)[span_15](end_span)
    assert module.is_palindrome_string("racecar") is True
    assert module.is_palindrome_string("hello") is False
    assert module.is_palindrome_string("A man a plan a canal Panama") is True
    assert module.is_palindrome_string("madam") is True
    
    # Required expected output[span_16](start_span)[span_16](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()