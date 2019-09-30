import requests
import
#Her importerer vi requests, som er et biblotek som kan håndtere at hente data fra en givent side

brugerLink = input("Hvilket link vil du have data fra?\n")
#Vi gør det muligt at man kan bruge alle links, men denne del er ikke nødvendigt hvis man allerede har et link

LixText = requests.get(brugerLink)
#Her importerer vi en side og definerer det til at være "LixText", men det er bare en variabel navn

#Vi får testet om linkets status code er 200, som betyder at siden er oppe.
if LixText.status_code == 200:
    #Hvis siden er oppe, definerer den det som text som en variabel
    t = LixText.text
    #Så bliver teksten printet
    print(t)
else:
    #Hvis siden ikke er oppe, så bliver der sagt at linket ikke er oppe og hvad dens status code er
    print("The status code of", brugerLink , "is", LixText.status_code)
    #Vi printer også hvad de top 10 status koder betyder, så folk ved hvad der sker
    indent = "  -  "
    statusCode = ["200 OK = You shouldn't be seeing this unless the code is broken, which means the link works", "201 Created = Fulfilled and resulted in a new resource being created.","204 No Content = The server succesfully processed the request, but is not returning any content","304 Not Modified = Resource has been modified since last visit.","400 Bad Request = The request cannot be fulfilled due to bad syntax.","401 Unauthorized = Request requires user authentication","403 Forbidden = The request was a legal request, but the server is refusing to respond to it","404 Not Found = The server has not found anything matching the Request-URI", "409 Conflict = The request could not be completed due to a conflict with the current state of the resource", "500 Internal Server Error = The server encountered an unexpected condition which prevented it from fulfilling the request."]
    print(indent+"200")


def dataFil():
    dataName = input("hvad skal filen som du gemmer hede?\n")
    f = open(dataName + ".txt")
    f.write(t)
    f.close()
