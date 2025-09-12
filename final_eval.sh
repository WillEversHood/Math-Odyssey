#!/bin/bash


for j in $(seq 1 $2); do
    correct=0
    wrong=0
    cd ~/Documents/Math-Odyssey-limits
    chmod +x stratified_sampling.py
    python3 stratified_sampling.py $1
    lines=$(wc -l < sample.jsonl)
    echo "number of problems $1"
    for i in $(seq 1 $1); do
        #echo "Line number: $i"
        cd ~/Documents/Math-Odyssey-limits
        chmod +x generate_question.py
        chmod +x generate_answer.py
        question=$(python3 generate_question.py $i)
        answer=$(python3 generate_answer.py $i)
        echo "problem: $i"
        #echo "answer: $answer"
        #echo "question: $question"
        
        cd ~/Documents/Math-Odyssey-limits/gen_formalizer
        chmod +x generate_score.py
        #crewai install
        #myarray=($question $answer)
        crewai run "$question" "$answer"
        cp attempt.txt sneakpeak.txt
        sed -n '/{/,/}/p' attempt.txt > attempt.json

        #mv attempt.txt attempt.json
        score=$(python3 generate_score.py)
        if [ "$score" == 1 ]; then
            let correct=correct+1
            echo "Proof is correct ✅"
        else
            echo "Proof is incorrect ❌"
            let wrong=wrong+1
        fi
    done
    echo "wrong: $wrong" >&2
    echo "correct: $correct" >&2
    echo "\n" >&2
done
