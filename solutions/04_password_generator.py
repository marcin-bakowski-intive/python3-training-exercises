"""
Write a password generator, which generates strong passwords as a mix of lowercase letters, uppercase letters, numbers,
and symbols. The passwords should be random, generating a new password every time the user asks for a new password.
"""
import random
import string

DEFAULT_CHARACTER_SET = string.ascii_letters + string.digits + string.punctuation


def generate_password(length=8, chars=DEFAULT_CHARACTER_SET):
    return "".join(random.choice(chars) for _ in range(length))


password_length = int(input("Password length: "))
if password_length < 8:
    print("Password to short")
else:
    print("Password: %s" % generate_password(password_length))
