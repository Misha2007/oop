"""School class which stores information about courses and students."""

from course import Course
from student import Student


class School:
    """Class course."""

    def __init__(self, name):
        """Konstruktor."""
        self.name = name
        self.courses = []
        self.student = []

    def add_course(self, course: Course):
        """Add new course."""
        if course not in self.courses:
            self.courses.append(course)

    def add_student(self, student: Student):
        """Add new student and set id."""
        if student not in self.student:
            student.set_id(len(self.student) + 1)
            self.student.append(student)

    def add_student_grade(self, student: Student, course: Course, grade: int):
        """Add grades."""
        if student in self.student and course in self.courses:
            student.grades.append((course, grade))
            course.grades.append((student, grade))

    def get_students(self) -> list[Student]:
        """Return students."""
        return self.student

    def get_courses(self) -> list[Course]:
        """Return courses."""
        return self.courses

    def get_students_ordered_by_average_grade(self) -> list[Student]:
        """Return students by average grade."""
        return sorted(self.student, key=lambda student: student.get_average_grade(), reverse=True)