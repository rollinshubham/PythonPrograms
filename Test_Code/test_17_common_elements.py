import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '17_common_elements.py'))
spec = importlib.util.spec_from_file_location("17_common_elements", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_15](start_span)[span_15](end_span)
    assert module.find_common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert module.find_common_elements(["a", "b"], ["c", "d"]) == []
    assert module.find_common_elements([], [1, 2]) == []
    
    # Required expected output[span_16](start_span)[span_16](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()