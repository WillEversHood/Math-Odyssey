# Math Odyssey Cost Optimization

This is a small example to show case the efficiency improvements made using Artemis to optimize for cost efficiency 

## 🚀 Quickstart

Follow these steps to get up and running quickly.

### 1. Clone the Repository

```bash
git clone https://github.com/WillEversHood/Math-Odyssey.git
cd Math-Odyssey
```
### 2. Install UV
see:
https://docs.astral.sh/uv/getting-started/installation/
### 3. Install Dependencies

```bash
cd gen_formalizer && uv sync
```

### 4. Run a Sample Script

This script 'final_eval.sh' manages the execution and evaluation of the problems from the math odysssey corpus.

```bash
cd .. && ./ final_eval.sh 30 2 2> output.txt
```

---

## 📘 Tutorial

To run a custom evaluation you can run

```command time -o -v time.log ./final_eval.sh <#problems per eval> <#evals> 2>output.txt```

### Step 1: Understand Reporting

**output.txt** tracks the number of correct problems which are updated at the end of each run. It als tracks any errors that occur while running the eval

**token_usage.txt** tracks the number of tokens used per request. For every problem there should be 2 requests.

**time.log** contains the performance metrics regarding the time taken to evaluate the benchmark.

## Step 2. To switch to Optimized Code 

### Refer to Project Structure

Switch optimized for non-optimized files renaming accordingly. The project can now be run exactly as it was before however this time you should see significant performance improvments and a significant. 

## 🧰 Project Structure

```
Math-Odyssey/
|- gen_formalizer/
|-|-src/
|-|-|-main.py
|-|-|-crew.py
|-|-|-crewOptimized.py
|-|-|-config/
|-|-|-|-tasks.yaml
|-|-|-|-tasksOptimized.yaml
|-|-|-|-agents.yaml
|-|-|-|-agentsOptimized.yaml
```

---