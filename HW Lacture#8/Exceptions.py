class Errors(Exception):
    pass


class CityNameError(Errors):
    error_message = ('City name must contain only letters')

    def __init__(self):
        super().__init__()
        self.msg = self.error_message

    def __str__(self):
        return self.msg


class CoordError(Errors):
    error_message = ("Invalid Coords. Try again")

    def __init__(self):
        super().__init__()
        self.msg = self.error_message

    def __str__(self):
        return self.msg



