import importlib.util
import os

# Dynamically load the module since it starts with a number
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Code', '03_pos_neg_zero.py'))
spec = importlib.util.spec_from_file_location("03_pos_neg_zero", file_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

def run_tests():
    # Write test cases using assert[span_3](start_span)[span_3](end_span)
    assert module.check_number(10) == "Positive"
    assert module.check_number(-5) == "Negative"
    assert module.check_number(0) == "Zero"
    assert module.check_number(3.14) == "Positive"
    assert module.check_number(-0.01) == "Negative"
    
    # Required expected output[span_4](start_span)[span_4](end_span)
    print("All test cases passed.")

if __name__ == "__main__":
    run_tests()