import math

class SimilarityCalculator:
    """Provides similarity calculation methods"""

    @staticmethod
    def cosine_similarity(vec1, vec2):
        """Compute cosine similarity between two vectors"""
        if not vec1 or not vec2 or len(vec1) != len(vec2):
            return 0.0

        dot_product = sum(a * b for a, b in zip(vec1, vec2))
        norm1 = math.sqrt(sum(a * a for a in vec1))
        norm2 = math.sqrt(sum(b * b for b in vec2))

        if norm1 == 0 or norm2 == 0:
            return 0.0

        return dot_product / (norm1 * norm2)

    @staticmethod
    def jaccard_similarity(set1, set2):
        """Compute Jaccard similarity between two sets"""
        if not set1 or not set2:
            return 0.0

        set1, set2 = set(set1), set(set2)

        intersection = len(set1.intersection(set2))
        union = len(set1.union(set2))

        return intersection / union if union != 0 else 0.0