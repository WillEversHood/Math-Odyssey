import json
def score():
    try:
        with open("attempt.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            print(data["score"])
    except Exception:
        print(0)
if __name__=='__main__':
    score()