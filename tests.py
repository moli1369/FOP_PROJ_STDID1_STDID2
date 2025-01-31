import unittest
from user_management import register, login
from course_management import create_course, add_student_to_course

class TestLMS(unittest.TestCase):
    def test_register(self):
        self.assertTrue(register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890'))
        self.assertFalse(register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890'))

    def test_login(self):
        register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890')
        self.assertIsNotNone(login('123', 'password'))
        self.assertIsNone(login('123', 'wrongpassword'))

    def test_create_course(self):
        self.assertTrue(create_course('C101', 'Python Programming', 'Learn Python', 'P001'))
        self.assertFalse(create_course('C101', 'Python Programming', 'Learn Python', 'P001'))

    def test_add_student_to_course(self):
        create_course('C101', 'Python Programming', 'Learn Python', 'P001')
        self.assertTrue(add_student_to_course('C101', '123'))
        self.assertFalse(add_student_to_course('C102', '123'))  # Course does not exist

if __name__ == "__main__":
    unittest.main()