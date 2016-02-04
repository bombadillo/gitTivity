import os

def createIfNotExists(dir):
    if not os.path.exists(dir):
        try:
            os.makedirs(dir)
        except OSError as exc:
            if exc.errno != errno.EEXIST:
                raise
