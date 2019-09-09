import re

class FileProperties(object):
    def __init__(self, filename):
        self.filename = filename

    def readFileAsRead(self):
        file = open(self.filename, "r")
        content = file.read()
        file.close()
        return content

    def readFileAsReadlines(self, removeSpace=False):
        file = open(self.filename, "r")
        content = file.read()
        file.close()

        print(content)

        content = content.split()

        """if(removeSpace == False):
            for e in range(len(content)):
                content[e] = content[e].strip("\n")
        else:
            for e in range(len(content)):
                content[e] = content[e].strip("\n")
                content[e] = content[e].split()
            for e in content:
                print(e)
                #content = e.split()
"""

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

    print(FileProperties("test.txt").readFileAsRead())
    print(FileProperties("test.txt").readFileAsReadlines(True))
