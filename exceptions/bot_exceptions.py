
class TokenNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("check the virtual environment for data about the API key for telegram")

class InvalidToken(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__("check the API key for validity")