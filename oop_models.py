
class User:
    def __init__(self, id, name, email, password, phone):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

class Student(User):
    def __init__(self, id, name, email, password, phone):
        super().__init__(id, name, email, password, phone)
        self.courses = []

class Professor(User):
    def __init__(self, id, name, email, password, phone):
        super().__init__(id, name, email, password, phone)
        self.courses_taught = []

class Course:
    def __init__(self, id, name, description, instructor):
        self.id = id
        self.name = name
        self.description = description
        self.instructor = instructor
        self.students = []
        self.grading_system = {}
        self.grades = {}

    def add_student(self, student):
        self.students.append(student)
        student.courses.append(self)

    def set_grading_system(self, grading_system):
        self.grading_system = grading_system

    def submit_grade(self, student_id, section, grade):
        if student_id not in self.grades:
            self.grades[student_id] = {}
        self.grades[student_id][section] = grade