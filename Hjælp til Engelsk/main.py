import requests

url = "https://wordsapiv1.p.rapidapi.com/words/incredible/definitions"

headers = {
    'x-rapidapi-host': "wordsapiv1.p.rapidapi.com",
    'x-rapidapi-key': "SIGN-UP-FOR-KEY"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)