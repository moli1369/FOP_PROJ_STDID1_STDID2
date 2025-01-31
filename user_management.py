import json

# ذخیره اطلاعات کاربران در فایل
def save_users(users, filename='users.json'):
    with open(filename, 'w') as f:
        json.dump(users, f)

# بارگیری اطلاعات کاربران از فایل
def load_users(filename='users.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

# ثبت‌نام کاربر جدید
def register(user_type, user_id, name, email, password, phone):
    users = load_users()
    if user_id in users:
        return False  # کاربر قبلاً ثبت‌نام کرده است
    users[user_id] = {
        'type': user_type,
        'name': name,
        'email': email,
        'password': password,
        'phone': phone
    }
    save_users(users)
    return True

# ورود کاربر
def login(user_id, password):
    users = load_users()
    if user_id in users and users[user_id]['password'] == password:
        return users[user_id]
    return None