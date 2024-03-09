import random
import string
# password_lenght = 16


def generate_password():
    generated_password = "".join(random.choices(string.ascii_letters +
                                                string.digits + string.punctuation, k=16))
    print(generated_password)


generate_password()
