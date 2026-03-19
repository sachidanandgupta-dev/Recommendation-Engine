from similarity import SimilarityCalculator

class Scorer:
    """Scores and ranks items"""

    def __init__(self, item_data):
        self.item_data = item_data

    def score(self, user_preferences, candidates):
        scores = {}

        for item in candidates:
            item_features = self.item_data.get(item, [])
            score = SimilarityCalculator.jaccard_similarity(
                user_preferences, item_features
            )
            scores[item] = score

        return scores

    def get_top_n(self, scores, n=3):
        if not scores:
            return []

        sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        return [item for item, _ in sorted_items[:n]]