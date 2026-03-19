# Recommendation Engine Core Components

## Overview
This project builds a simple recommendation engine using basic algorithms.

It demonstrates how systems recommend items using:
- Similarity calculation
- Candidate filtering
- Ranking
- Evaluation

---

## Components

### 1. Similarity Calculator
- Cosine Similarity
- Jaccard Similarity

### 2. Candidate Generator
Filters items based on user preferences.

### 3. Scorer
Ranks items using similarity scores.

### 4. Evaluator
Measures performance using Precision.

---

## How It Works

1. Input user preferences
2. Generate candidate items
3. Calculate similarity scores
4. Rank items
5. Evaluate recommendations

---

## Example Output

Candidates:
['item1', 'item3', 'item5']

Scores:
{'item1': 0.5, 'item3': 0.33, 'item5': 1.0}

Top Recommendations:
['item5', 'item1', 'item3']

Precision:
1.0

---

## Features

- Modular design
- Handles edge cases
- Beginner-friendly
- Easy to extend

---

## Run Instructions
python main.py
