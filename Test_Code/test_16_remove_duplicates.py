import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '16_remove_duplicates.py'))
spec = importlib.util.spec_from_file_location("16_remove_duplicates", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_9](start_span)[span_9](end_span)
    assert module.remove_duplicates([1, 2, 2, 3, 4, 4]) == [1, 2, 3, 4]
    assert module.remove_duplicates(["apple", "apple", "banana"]) == ["apple", "banana"]
    assert module.remove_duplicates([]) == []
    
    # Required expected output[span_10](start_span)[span_10](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()