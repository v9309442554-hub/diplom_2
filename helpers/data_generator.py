import random
import string

from helpers.test_data import PASSWORD_LENGTH, USER_NAME


def generate_user_data():
    email = f"qa_{random.randint(100000, 999999)}@example.com"
    password = "".join(random.choices(string.ascii_letters + string.digits, k=PASSWORD_LENGTH))
    return {"email": email, "password": password, "name": USER_NAME}
