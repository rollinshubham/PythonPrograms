import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '15_second_largest.py'))
spec = importlib.util.spec_from_file_location("15_second_largest", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.find_second_largest([10, 20, 4, 45, 99]) == 45
    assert module.find_second_largest([10, 10, 10]) is None
    assert module.find_second_largest([5]) is None
    assert module.find_second_largest([-5, -1, -10]) == -5
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()