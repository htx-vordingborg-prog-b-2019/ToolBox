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

<<<<<<< HEAD

def dataFil():
    dataName = input("hvad skal filen som du gemmer hede?\n")
    f = open(dataName + ".txt")
    f.write(t)
    f.close()
=======
#Denne del nedenunder, er optional, den tager den text som du har fået fra din side, og laver den om til en fil.
>>>>>>> 161217d313bb5f3545a5f726bd5b8acb2163d703
