from collections import namedtuple

# مدل دانشجو
Student = namedtuple('Student', ['id', 'name', 'email', 'password', 'phone'])

# مدل استاد
Professor = namedtuple('Professor', ['id', 'name', 'email', 'password', 'phone'])

# مدل دوره آموزشی
Course = namedtuple('Course', ['id', 'name', 'description', 'instructor_id', 'students_ids'])