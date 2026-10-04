import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '19_find_duplicates.py'))
spec = importlib.util.spec_from_file_location("19_find_duplicates", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_9](start_span)[span_9](end_span)
    result1 = module.find_duplicates([1, 2, 2, 3, 4, 4, 5])
    assert sorted(result1) == [2, 4]
    assert module.find_duplicates([1, 2, 3]) == []
    assert module.find_duplicates([]) == []
    
    # Required expected output[span_10](start_span)[span_10](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()