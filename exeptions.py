class KeywordError(Exception):
    """Expected another keyword or symbol"""

    def __init__(self, msg=""):
        self.msg = msg


class IdError(Exception):
    """Identifier is keyword"""

    def __init__(self, msg=""):
        self.msg = msg


class StateError(Exception):
    """Invalid state"""

    def __init__(self, msg=""):
        self.msg = msg