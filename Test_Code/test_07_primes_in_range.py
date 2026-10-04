import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '07_primes_in_range.py'))
spec = importlib.util.spec_from_file_location("07_primes_in_range", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.get_primes_in_range(1, 10) == [2, 3, 5, 7]
    assert module.get_primes_in_range(10, 20) == [11, 13, 17, 19]
    assert module.get_primes_in_range(24, 25) == []
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()