#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from gen_formalizer.crew import GenFormalizer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run(math, answer):
    """
    Run the crew.
    """
    inputs = {
        'topic': math,
        'current_year': str(datetime.now().year),
        'answer': answer
    }
    
    try:
        print('Hello')
        print(math)
        result = GenFormalizer().crew().kickoff(inputs=inputs)
        # Get token usage
        token_usage = result.token_usage  # usually a dict
        # Write token usage to a file
        with open("token_usage.txt", "a") as f:
            print(token_usage)
            f.write(str(token_usage))
            f.write("\n")
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        GenFormalizer().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        GenFormalizer().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    
    try:
        GenFormalizer().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")
