import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '11_vowels_consonants.py'))
spec = importlib.util.spec_from_file_location("11_vowels_consonants", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.count_vowels_consonants("hello") == (2, 3)
    assert module.count_vowels_consonants("Python") == (1, 5)
    assert module.count_vowels_consonants("AEIOU") == (5, 0)
    assert module.count_vowels_consonants("123 !!") == (0, 0)
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()