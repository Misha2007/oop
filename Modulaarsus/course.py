"""Course class with name and grades."""


class Course:
    """Class course."""

    def __init__(self, name: str):
        """Konstruktor."""
        self.name = name
        self.grades = list()

    def get_grades(self):
        """Return one course's grades."""
        return self.grades

    def get_average_grade(self) -> float:
        """Return one course's average grade."""
        all_grades = 0
        if not self.grades:
            return -1
        for i in self.grades:
            all_grades += i[1]
        return all_grades / len(self.grades)

    def __repr__(self):
        """Return function."""
        return self.name