import json

# ذخیره اطلاعات نمرات در فایل
def save_grades(grades, filename='grades.json'):
    with open(filename, 'w') as f:
        json.dump(grades, f)

# بارگیری اطلاعات نمرات از فایل
def load_grades(filename='grades.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# تعیین بارم‌بندی دوره
def set_grading_system(course_id, grading_system):
    grades = load_grades()
    grades[course_id] = {'grading_system': grading_system, 'students': {}}
    save_grades(grades)
    return True

# ثبت نمره دانشجو
def submit_grade(course_id, student_id, section, grade):
    grades = load_grades()
    if course_id in grades:
        if student_id not in grades[course_id]['students']:
            grades[course_id]['students'][student_id] = {}
        grades[course_id]['students'][student_id][section] = grade
        save_grades(grades)
        return True
    return False