"""
requestTutorial er en skabelon til hvordan man kan hente og vise ens data. Det er et eksempel og kan laves på andre måder.

Programmet her er beregnet til plain text!!!

Lavet af Lukas 3.R og Simon Julendal 3.R
Vi er næsten ligeså seje som McCool
"""

import requests
#Her importerer vi requests, som er et biblotek som kan håndtere at hente data fra en givent side

brugerLink = input("Hvilket link vil du have data fra?\n")
#Vi gør det muligt at man kan bruge alle links, men denne del er ikke nødvendigt hvis man allerede har et link

LixText = requests.get(brugerLink)
#Her importerer vi en side og definerer det til at være "LixText", men det er bare en variabel navn

'''
Denne del er kun vigtigt hvis du vil have den til at downloade ens side
'''
def dataFil(): #Jeg definerer dataFil til at være en funktion, hvor at jeg bare kan kalde på den når der skal downloades som en fil
    dataName = str(input("hvad skal filen som du gemmer hede?\n")) #Her spørger vi hvad filen skal hede (ikke nødvendigt)
    f = open(dataName + ".txt", "w") #Vi åbner filen i "w" som gør at vi kan lave en fil og ændre i den. Navnet kommer fra før, men man kan selv bestemme hvad navnet skal være
    f.write(t) #Her sætter vi teksten fra hjemmesiden ind i dokumentet
    f.close() #Vi lukker filen, fordi at det er MEGET vigtigt efter man har åbnet den, ellers SKAL du genstarte din computer

#Vi får testet om linkets status code er 200, som betyder at siden er oppe.
if LixText.status_code == 200:
    #Hvis siden er oppe, definerer den det som text i en variabel
    t = LixText.text
    #Så bliver teksten printet
    print(t)

    #Så har vi valgt at tilføje at man kan have lov til at gemme filen, hvis man har lyst.
    #Det gøres ved at brugeren bliver spurgt om deres fil skal gemmes
    choice = input("Har du lyst til at gemme filen?(Y/N)\n")
    #hvis svaret så er ja, eller "Y", så sender den videre til dataFil() funktionen
    if choice == "Y":
        dataFil()
else:
    #Hvis siden ikke er oppe, så bliver der sagt at linket ikke er oppe og hvad dens status code er
    print("The status code of", brugerLink , "is", LixText.status_code)
    #Vi printer også hvad de top 10 status koder betyder, så folk ved hvad der sker
    xd = 0
    indent = "  -  "
    #Vi laver et biblotek med de top 10 status koder som den skal printe
    statusCode = ["200 OK = You shouldn't be seeing this unless the code is broken, which means the link works", "201 Created = Fulfilled and resulted in a new resource being created.","204 No Content = The server succesfully processed the request, but is not returning any content","304 Not Modified = Resource has been modified since last visit.","400 Bad Request = The request cannot be fulfilled due to bad syntax.","401 Unauthorized = Request requires user authentication","403 Forbidden = The request was a legal request, but the server is refusing to respond to it","404 Not Found = The server has not found anything matching the Request-URI", "409 Conflict = The request could not be completed due to a conflict with the current state of the resource", "500 Internal Server Error = The server encountered an unexpected condition which prevented it from fulfilling the request."]
    for i in statusCode: #Så printer vi alle statuskoderne med et indent
        print(indent + statusCode[xd]+"\n")
        xd=xd+1
