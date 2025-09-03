import sys
import json
def process_math_problems(input_file, stop):
     # Initialize your solving class
    key = f"Problem_{stop}"
    with open(input_file, "r", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line)   # parse one JSON object
            if key in data:
                print(data[key]["answer"])
                return  # return the question field
            
if __name__ == '__main__':
    process_math_problems('final-odyssey-math-with-levels.jsonl', sys.argv[1])  