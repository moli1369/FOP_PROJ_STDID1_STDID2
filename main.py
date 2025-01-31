from user_management import register, login
from course_management import create_course, add_student_to_course
from grading import set_grading_system, submit_grade
from reports import generate_class_list

def main():
    # مثال استفاده از توابع
    register('student', '123', 'John Doe', 'john@example.com', 'password', '1234567890')
    user = login('123', 'password')
    if user:
        print("Login successful!")
    
    create_course('C101', 'Python Programming', 'Learn Python', 'P001')
    add_student_to_course('C101', '123')
    
    set_grading_system('C101', {'Quiz1': 20, 'Midterm': 30, 'Final': 50})
    submit_grade('C101', '123', 'Quiz1', 18)
    
    df = generate_class_list('C101')
    print(df)

if __name__ == "__main__":
    main()