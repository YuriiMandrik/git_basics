from .system_helpers import save_to_file, get_file_data, save_list_to_file
from .decorators_helpers import is_email_valid


@is_email_valid
def save(
        email, first_name, last_name,
        phone, work_id, type):
    new_employee = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "work_id": work_id,
        "type": type,
    }
    save_to_file(new_employee, "database/employees.json")


def update(id):
    employers = get_file_data("database/employees.json")
    for employee in employers:
        if id == employee["id"]:
            employee["email"] = input("Email: ")
            employee["first_name"] = input("First name: ")
            employee["last_name"] = input("Last Name: ")
            employee["phone"] = input("Phone: ")
            employee["work_id"] = input("Work id: ")
            employee["type"] = input("type: ")

    save_list_to_file(employers, "database/employees.json")


def get_all_employers():
    employees = get_file_data("database/employees.json")
    for employee in employees:
        print(employee["email"])
        print(employee["first_name"])
        print(employee["last_name"])
        print(employee["phone"])
        print(employee["work_id"])
        print(employee["type"])


def get_employee_by_email(email):
    employees = get_file_data("database/employees.json")
    for employee in employees:
        if employee["email"] == email:
            print(employee["email"])
            print(employee["first_name"])
            print(employee["last_name"])
            print(employee["phone"])
            print(employee["work_id"])
            print(employee["type"])
            return employee


def save_plant(name, address):
    new_plant = {"name": name, "address": address}
    save_to_file(new_plant, "database/plants.json")


def get_all_plants():
    plants = get_file_data("database/plants.json")
    for plant in plants:
        print(plant["name"])
        print(plant["address"])


def get_plant_by_id(id):
    plants = get_file_data("database/plants.json")
    for plant in plants:
        if plant["id"] == id:
            print(plant["name"])
            print(plant["address"])


def save_salon(name, address):
    new_el = {"name": name, "address": address}
    save_to_file(new_el, "database/salons.json")


def get_salon_by_id(id):
    salons = get_file_data("database/salons.json")
    for salon in salons:
        if salon["id"] == id:
            print(salon["name"])
            print(salon["address"])


def save_sales_departament(name, address):
    new_s_d = {"name": name, "address": address}
    save_to_file(new_s_d, "database/sales_departament.json")


def get_sales_departament_by_id(id):
    sales_departament = get_file_data("database/sales_departament.json")
    for s_d in sales_departament:
        if s_d["id"] == id:
            print(s_d["name"])
            print(s_d["address"])


def delete_employee(id):
    employees = get_file_data("database/employees.json")
    for i in range(len(employees)):
        if id == employees[i]["id"]:
            del employees[i]
            break
    save_list_to_file(employees, "database/employees.json")