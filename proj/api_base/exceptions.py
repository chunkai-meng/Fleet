

class APIException(Exception):
    code = 0  # type: int
    message = ""  # type: str

    def __init__(self, message=None, code=None):
        super().__init__()
        if message is not None:
            self.message = message
        if code is not None:
            self.code = code
