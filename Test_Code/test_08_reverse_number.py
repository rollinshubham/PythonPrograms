import importlib.util
import os

file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '08_reverse_number.py'))
spec = importlib.util.spec_from_file_location("08_reverse_number", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_9](start_span)[span_9](end_span)
    assert module.reverse_number(1234) == 4321
    assert module.reverse_number(-567) == -765
    assert module.reverse_number(100) == 1
    assert module.reverse_number(0) == 0
    
    # Required expected output[span_10](start_span)[span_10](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()