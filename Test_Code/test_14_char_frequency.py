import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '14_char_frequency.py'))
spec = importlib.util.spec_from_file_location("14_char_frequency", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.char_frequency("hello") == {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    assert module.char_frequency("aaa") == {'a': 3}
    assert module.char_frequency("") == {}
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()