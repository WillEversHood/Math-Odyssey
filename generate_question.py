import sys
import json
def process_math_problems(input_file, stop):
  
     # Initialize your solving class
    with open(input_file, "r", encoding="utf-8") as f:
        
        for i , line in enumerate(f, start=1):
            if i == int(stop):
                
                data = json.loads(line)   # parse one JSON object
                inner_val = list(data.values())[0]
                print(inner_val['question'])
                return  # return the question field


             

if __name__ == '__main__':
    process_math_problems('sample.jsonl', sys.argv[1])  