import time


def base_decorator(j):
    def iterator(func):
        def wrapper(x, y):
            print(j)
            start_time = time.time()
            func(x, y)
            print(time.time() - start_time)

        return wrapper
    return iterator


@base_decorator(5)
def suma(x, y):
    print(x + y)



@base_decorator(123)
def minus(x, y):
    print(x - y)


minus(8, 2)
suma(8, 2)


class A:
    @staticmethod
    def hello():
        print("hello")
