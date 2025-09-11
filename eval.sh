#!/bin/bash
cd ~/Documents/Math-Odyssey
if [ "$1" = "light" ]; then
    dir="-light"
elif [ "$1" = "vlight" ]; then
    dir="-vlight"
elif [ "$1" = "ulight" ]; then
    dir="-ulight"
elif [ "$1" = "mlight" ]; then
    dir="-mlight"
else
    dir=""
fi
file="final-odyssey-math-with-levels"$dir".jsonl"
correct=0
wrong=0
lines=$(wc -l < $file)
echo "number of problems $lines"
for i in $(seq 1 $lines); do
    #echo "Line number: $i"
    cd ~/Documents/Math-Odyssey
    chmod +x generate_question.py
    chmod +x generate_answer.py
    question=$(python3 generate_question.py $i)
    answer=$(python3 generate_answer.py $i)
    echo "problem: $i"
    #echo "answer: $answer"
    #echo "question: $question"
    
    cd ~/Documents/Math-Odyssey/gen_formalizer
    chmod +x generate_score.py
    crewai install
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
echo "wrong: $wrong"
echo "correct: $correct"

