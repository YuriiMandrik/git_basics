import json


def get_file_data(path):
    try:
        file = open(path, "r")
        try:
            data_list = json.loads(file.read())
            return data_list
        except:
            print("Error while working with the file")
        finally:
            file.close()
    except FileNotFoundError:
        print("File not found")


def save_list_to_file(data, path):
    try:
        file = open(path, "w")
        try:
            data_in_json = json.dumps(data)
            file.write(data_in_json)
        except :
            print("Error while working with the file")
        finally:
            file.close()
    except FileNotFoundError:
        print("File not found")


def save_to_file(data: dict, path: str):
    data_list = get_file_data(path)
    try:
        if len(data_list) < 1:
            data["id"] = 1
        else:
            data["id"] = len(data_list) + 1
        data_list.append(data)
        save_list_to_file(data_list, path)
    except TypeError:
        #цю помилку ловимо у випадку коли файл для запису повністю пустий( не містить навіть пустого списку)
        print("It seems that a non-json file was used for recording")

