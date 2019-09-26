import requests
#Her importerer vi requests, som er et biblotek som kan håndtere at hente data fra en givent side
brugerLink = input("Hvilket link vil du have data fra?")
LixText = requests.get(brugerLink)
#Her importerer vi en side og definerer det til at være "LixText", men det er bare en variabel navn

t = LixText.text

print(t)
