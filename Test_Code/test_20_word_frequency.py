import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '20_word_frequency.py'))
spec = importlib.util.spec_from_file_location("20_word_frequency", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_15](start_span)[span_15](end_span)
    assert module.get_word_frequency("hello world hello") == {"hello": 2, "world": 1}
    assert module.get_word_frequency("test test test") == {"test": 3}
    assert module.get_word_frequency("") == {}
    
    # Required expected output[span_16](start_span)[span_16](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()