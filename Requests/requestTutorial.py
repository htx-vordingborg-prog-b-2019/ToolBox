import requests
#Her importerer vi requests, som er et biblotek som kan håndtere at hente data fra en givent side

LixText = requests.get('https://drive.google.com/drive/u/0/my-drive')
#Her importerer vi en side og definerer det til at være "LixText", men det er bare en variabel navn

t = LixText.text

print(t)
