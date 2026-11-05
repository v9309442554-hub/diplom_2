import random
import string


def generate_user_data():
    email = f"qa_{random.randint(100000, 999999)}@example.com"
    password = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    return {"email": email, "password": password, "name": "QA User"}
