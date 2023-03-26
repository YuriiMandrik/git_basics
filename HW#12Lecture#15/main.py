import threading
from urllib.request import urlopen
import json


def get_course(url):
    response = urlopen(url).read().decode('utf-8')
    res = json.loads(response)
    return res


def get_course_pb():
    url = "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5"
    res = get_course(url)
    #print(res[1]['buy'])
    return res[1]['buy']


def get_course_nbu():
    url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json'
    res = get_course(url)
    #print(res[24]['rate'])
    return res[24]['rate']


def get_best_course():

    print (f'Best course is {max(float(get_course_pb()), float(get_course_nbu()))}')
    return max(float(get_course_pb()), float(get_course_nbu()))



if __name__ == "__main__":
        thread1 = threading.Thread(target=get_course_pb)
        thread2 = threading.Thread(target=get_course_nbu)
        thread3 = threading.Thread(target=get_best_course)

        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()
        thread3.start()

