class TranslError(Exception):
    """Expected another keyword or symbol"""

    def __init__(self, msg=""):
        self.msg = msg


class SyntaxUnitError(Exception):
    """Expected another keyword or symbol"""

    def __init__(self, msg=""):
        self.msg = msg


class IdUnitError(Exception):
    """Identifier is keyword"""

    def __init__(self, msg=""):
        self.msg = msg


class StateError(Exception):
    """Invalid state"""

    def __init__(self, msg=""):
        self.msg = msg


class LexicalUnitError(Exception):
    """Отвечает за ошибки в лексическом блоке"""

    def __init__(self, expected, char, state):
        msg = f"Expected {expected}, but received {char} on state {state}"
        self.msg = msg
