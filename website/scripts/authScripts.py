import string
import random


def emailValidation(email):
    if (email.count('@') > 0) and (email.count('.') > 0) and len(email) > 4:
        return True
    return False


def passwordValidation(password1, password2):
    if (password1 == password2) and (len(password1) > 5):
        return True
    return False


def defaultNick(email):
    output = ''
    for letter in email:
        if letter == '@':
            break
        output += letter
    return output


def confirm_key_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
