import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '18_missing_number.py'))
spec = importlib.util.spec_from_file_location("18_missing_number", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.find_missing_number([1, 2, 4, 5], 5) == 3
    assert module.find_missing_number([1, 3, 4], 4) == 2
    assert module.find_missing_number([2, 3, 4, 5], 5) == 1
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()