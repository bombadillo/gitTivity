import os

def remove(fileName):
    if os.path.exists(fileName):
        os.remove(fileName)
