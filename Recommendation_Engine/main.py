from candidate_generator import CandidateGenerator
from scorer import Scorer
from evaluator import Evaluator

def main():
    # Sample dataset
    item_data = {
        "item1": ["action", "adventure"],
        "item2": ["romance", "drama"],
        "item3": ["action", "thriller"],
        "item4": ["comedy"],
        "item5": ["action", "comedy"]
    }

    # User preferences
    user_preferences = ["action", "comedy"]

    # Ground truth (relevant items)
    relevant_items = ["item1", "item3", "item5"]

    # Step 1: Generate candidates
    generator = CandidateGenerator(item_data)
    candidates = generator.generate(user_preferences)

    # Step 2: Score candidates
    scorer = Scorer(item_data)
    scores = scorer.score(user_preferences, candidates)

    # Step 3: Get top recommendations
    top_items = scorer.get_top_n(scores, n=3)

    # Step 4: Evaluate
    precision_score = Evaluator.precision(top_items, relevant_items)

    # Output
    print("Candidates:", candidates)
    print("Scores:", scores)
    print("Top Recommendations:", top_items)
    print("Precision:", precision_score)


if __name__ == "__main__":
    main()