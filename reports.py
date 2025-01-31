import pandas as pd
from course_management import load_courses  # وارد کردن تابع load_courses
from grading import load_grades  # وارد کردن تابع load_grades

# تولید لیست دانشجویان و نمرات آن‌ها
def generate_class_list(course_id):
    courses = load_courses()  # بارگیری اطلاعات دوره‌ها
    grades = load_grades()  # بارگیری اطلاعات نمرات
    
    if course_id not in courses or course_id not in grades:
        return None  # اگر دوره یا نمرات وجود نداشته باشد، None برگردان
    
    students_ids = courses[course_id]['students_ids']
    grading_system = grades[course_id]['grading_system']
    students_grades = grades[course_id]['students']
    
    data = []
    for student_id in students_ids:
        student_grades = students_grades.get(student_id, {})
        row = [student_id]
        for section in grading_system:
            row.append(student_grades.get(section, 0))
        data.append(row)
    
    columns = ['Student ID'] + list(grading_system.keys())
    df = pd.DataFrame(data, columns=columns)
    return df