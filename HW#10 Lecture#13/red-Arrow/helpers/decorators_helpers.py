
def is_email_valid(func):
    def wrapper(email, y, a, z, b, c):
        if "@" in email:
            if "." in email.split("@")[1]:
                func(email, y, a, z, b, c)
            else:
                print("Email invalid without dot!!!!")
        else:
            print("Email invalid without @ !!!!")
    return wrapper

