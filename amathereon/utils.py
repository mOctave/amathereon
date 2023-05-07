"""
A file containing extra utility scripts that are used in other places.
"""

class Completion(Exception):
    """
    An exception that is meant to allow for more complicated procedures than Python 'break' allows.
    """
    
    def __init__(self, message="Uncaught completion raised, you may be missing an 'except' statement."):
        self.message = message
        super().__init__(self.message)
