class Evaluator:
    """Evaluates recommendation quality"""

    @staticmethod
    def precision(recommended, relevant):
        if not recommended:
            return 0.0

        recommended_set = set(recommended)
        relevant_set = set(relevant)

        true_positive = len(recommended_set.intersection(relevant_set))

        return true_positive / len(recommended_set)