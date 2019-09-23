import re

class FileProperties(object):
    def __init__(self, filename):
        self.filename = filename

    def readFileAsString(self):
        file = open(self.filename, "r")
        content = file.read()
        file.close()
        return content

    def readFileAsList(self):
        file = open(self.filename, "r")
        content = file.read()
        file.close()

        content = content.split()

        return content

    def createFile(self):
        file = open(self.filename, "x")

    def writeToFile(self, content):
        file = open(self.filename, "a")
        file.write(content)
        file.close()

    def overwriteToFile(self, content):
        file = open(self.filename, "w")
        file.write(content)
        file.close()

if __name__ == "__main__":

    print(FileProperties("test.txt").readFileAsString())
    print(FileProperties("test.txt").readFileAsList())
