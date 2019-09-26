import requests
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
