import unittest
import os
from user_management import register, login
from course_management import create_course, add_student_to_course

class TestLMS(unittest.TestCase):
    def setUp(self):
        # حذف فایل‌های JSON قبل از هر تست
        if os.path.exists('users.json'):
            os.remove('users.json')
        if os.path.exists('courses.json'):
            os.remove('courses.json')

    def test_register(self):
        # تست ثبت‌نام کاربر جدید
        self.assertTrue(register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890'))
        
        # تست ثبت‌نام کاربری که قبلاً ثبت‌نام کرده است
        self.assertFalse(register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890'))

    def test_login(self):
        # ثبت‌نام یک کاربر جدید
        register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890')
        
        # تست ورود موفق
        self.assertIsNotNone(login('123', 'password'))
        
        # تست ورود ناموفق (رمز عبور اشتباه)
        self.assertIsNone(login('123', 'wrongpassword'))

    def test_create_course(self):
        # تست ایجاد دوره جدید
        self.assertTrue(create_course('C101', 'Python Programming', 'Learn Python', 'P001'))
        
        # تست ایجاد دوره‌ای که قبلاً وجود دارد
        self.assertFalse(create_course('C101', 'Python Programming', 'Learn Python', 'P001'))

    def test_add_student_to_course(self):
        # ایجاد یک دوره جدید
        create_course('C101', 'Python Programming', 'Learn Python', 'P001')
        
        # اضافه کردن دانشجو به دوره
        self.assertTrue(add_student_to_course('C101', '123'))
        
        # اضافه کردن دانشجو به دوره‌ای که وجود ندارد
        self.assertFalse(add_student_to_course('C102', '123'))  # Course does not exist

if __name__ == "__main__":
    unittest.main()