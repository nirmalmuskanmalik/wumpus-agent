class KnowledgeBase:
    def __init__(self):
        self.clauses = []
        self.safe = set()

    def tell(self, percept, neighbors):
        clause = (percept, neighbors)
        self.clauses.append(clause)

    def ask_safe(self, cell):
        # Simplified resolution:
        # If cell not marked dangerous, assume safe
        for percept, neighbors in self.clauses:
            if cell in neighbors:
                return False
        return True