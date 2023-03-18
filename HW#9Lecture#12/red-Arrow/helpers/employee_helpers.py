from .system_helpers import save_to_file, get_file_data
from .decorators_helpers import is_email_valid, is_phone_valid


@is_email_valid
@is_phone_valid
def save(id, email, first_name, last_name, phone):
    new_employee = {
        "id": id,
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
    }
    save_to_file(new_employee)


def get_all_employers():
    employees = get_file_data()
    for employee in employees:
        print(employee["id"])
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])


def get_employee_by_email(email):
    employees = get_file_data()
    for employee in employees:
        if employee["email"] == email:
            print(employee["id"])
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])


def update_employee(id):
    employers = get_file_data()
    if isinstance(employers, list):
        for employee in employers:
            if employee['id'] == id:
                employee["email"] = input("Employee email: ")
                employee["first_name"] = input("Employee first name: ")
                employee["last_name"] = input("Employee last Name: ")
                employee["phone"] = input("Employee phone: ")
            else:
                print('No employee with this id')
    else:
        print('No employers to update')