
def is_email_valid(func):
    def wrapper(x, email, y, a, z):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(x, email, y, a, z)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper


def is_phone_valid(func):
    def wrapper(x, y, a, z, phone):
        if len(phone) == 13:
            if phone[0] == '+':
                func(x, y, a, z, phone)
            else:
                print('Phone number is wrong. It must start with +')
        else:
            print('Wrong phone number length. It must have 12 digits')
    return wrapper




