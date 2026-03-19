class CandidateGenerator:
    """Generates candidate items based on user preferences"""

    def __init__(self, item_data):
        self.item_data = item_data

    def generate(self, user_preferences):
        if not user_preferences:
            return []

        candidates = []

        for item, features in self.item_data.items():
            if any(pref in features for pref in user_preferences):
                candidates.append(item)

        return candidates