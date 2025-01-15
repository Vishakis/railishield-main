import pandas as pd
import re

def split_number_dash(input_string):
    curr_match = re.match(r"(-?\d+\.?\d*)-(-?\d+\.?\d*)", input_string)
    if curr_match:
        return [int(float(curr_match.group(1))), int(float(curr_match.group(2)))]
    else:
        return input_string