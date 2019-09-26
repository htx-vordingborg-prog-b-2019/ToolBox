#Læs alt indhold i en fil
def readFile(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()
    return content

#Læs alt indhold i en fil, som en liste.
def readFileAsList(filename):
    file = open(filename, "r")
    content = file.read()
    file.close()

    content = content.split()

    return content

#Lav en fil
def createFile(filename):
    file = open(filename, "x")

#Skriv til en fil. Det skrevet indhold (content) bliver placeret bagerst i filen.
def writeToFile(filename, content):
    file = open(filename, "a")
    file.write(content)
    file.close()

#Erstat alt i filen, som bliver skrevet i content
def overwriteToFile(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

if __name__ == "__main__":

    #              "filename"
    print(readFile("test.txt"))
    print(readFileAsList("test.txt"))
#               "filename"   "content"  
    writeToFile("hol.txt", "Hej med dig!")
