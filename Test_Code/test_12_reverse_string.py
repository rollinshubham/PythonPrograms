import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '12_reverse_string.py'))
spec = importlib.util.spec_from_file_location("12_reverse_string", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_9](start_span)[span_9](end_span)
    assert module.reverse_string("hello") == "olleh"
    assert module.reverse_string("Python") == "nohtyP"
    assert module.reverse_string("") == ""
    assert module.reverse_string("a") == "a"
    
    # Required expected output[span_10](start_span)[span_10](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()