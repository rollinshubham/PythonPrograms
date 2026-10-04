import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '05_fibonacci_series.py'))
spec = importlib.util.spec_from_file_location("05_fibonacci_series", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.generate_fibonacci(0) == []
    assert module.generate_fibonacci(1) == [0]
    assert module.generate_fibonacci(5) == [0, 1, 1, 2, 3]
    assert module.generate_fibonacci(7) == [0, 1, 1, 2, 3, 5, 8]
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()