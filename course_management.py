import json

# ذخیره اطلاعات دوره‌ها در فایل
def save_courses(courses, filename='courses.json'):
    with open(filename, 'w') as f:
        json.dump(courses, f)

# بارگیری اطلاعات دوره‌ها از فایل
def load_courses(filename='courses.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ایجاد دوره جدید
def create_course(course_id, name, description, instructor_id):
    courses = load_courses()
    if course_id in courses:
        return False  # دوره قبلاً ایجاد شده است
    courses[course_id] = {
        'name': name,
        'description': description,
        'instructor_id': instructor_id,
        'students_ids': []
    }
    save_courses(courses)
    return True

# اضافه کردن دانشجو به دوره
def add_student_to_course(course_id, student_id):
    courses = load_courses()
    if course_id in courses:
        courses[course_id]['students_ids'].append(student_id)
        save_courses(courses)
        return True
    return False