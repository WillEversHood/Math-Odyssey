import json
import random
from collections import defaultdict
import sys

def create_samples(size):
    print('creating_samples', size)

    # Load JSONL objects (unwrap inner problem dict but keep outer key)
    data = []
    with open("final-odyssey-math-with-levels.jsonl", "r") as f:
        for line in f:
            outer = json.loads(line)       # {"Problem_1": {...}}
            problem_id, inner = list(outer.items())[0]
            data.append((problem_id, inner))

    # Group objects by (label, level) combination
    groups = defaultdict(list)
    for problem_id, obj in data:
        key = (obj["label"], obj["level"])
        groups[key].append((problem_id, obj))

    # Desired sample size
    sample_size = int(size)

    # Compute sample size per subgroup proportionally
    total = len(data)
    sample = []
    for key, objs in groups.items():
        k = round(len(objs) / total * sample_size)
        if k > 0:
            sample.extend(random.sample(objs, min(k, len(objs))))

    # Save sampled data back to JSONL
    with open("sample.jsonl", "w") as f:
        for problem_id, obj in sample:
            json_line = json.dumps({problem_id: obj})
            f.write(json_line + "\n")





if __name__=="__main__":
    create_samples(sys.argv[1])
