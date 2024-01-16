"""Student class with student name and grades."""


class Student:
    """Class course."""

    def __init__(self, name: str):
        """Konstruktor."""
        self.name = name
        self.grades = list()
        self.id = None

    def set_id(self, id: int):
        """Student gives id."""
        if self.id is None:
            self.id = id

    def get_id(self) -> int:
        """Return student's id."""
        return self.id

    def get_grades(self):
        """Return one student's grades."""
        return self.grades

    def get_average_grade(self):
        """Return one student's average grade."""
        all_grades = 0
        if not self.grades:
            return -1
        for i in self.grades:
            all_grades += i[1]
        return all_grades / len(self.grades)

    def __repr__(self) -> str:
        """Return function."""
        return self.name