import os


def get_cwd():
    path = os.path.dirname(os.path.abspath(__file__))
    # get absolute path
    return path
