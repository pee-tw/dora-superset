

class Sprint:
    def __init__(self, id, completedIssues, issuesNotCompletedInCurrentSprint) -> None:
        self.id = id
        self.completedIssues = completedIssues
        self.issuesNotCompletedInCurrentSprint = issuesNotCompletedInCurrentSprint