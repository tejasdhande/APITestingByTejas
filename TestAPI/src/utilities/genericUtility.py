import logging as logger
import random
import string

def generate_random_email_and_password(domain=None, email_prefix=None):
    logger.debug("Generating random email and password")

    if not domain:
        domain = "gmail.com"

    if not email_prefix:
        email_prefix = "testuser"

    random_email_string_length = 10

    random_string = "".join(random.choices(string.ascii_lowercase, k=random_email_string_length))

    email = email_prefix + '_' + random_string + '@' + domain

    password_length = 20

    random_password = "".join(random.choices(string.ascii_lowercase, k=password_length))

    random_info = {'email':email,'password':random_password}

    logger.debug(f"Random email and password generated:{random_info}")

    return random_info


