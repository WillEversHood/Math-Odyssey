import json
def score():
    with open("attempt.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print(data["score"])

if __name__=='__main__':
    score()