import directoryHandler
import os

def writeString(string, fileName):
    directoryHandler.createIfNotExists(os.path.dirname(fileName))
    with open(fileName, 'a') as the_file:
        the_file.write(string)
