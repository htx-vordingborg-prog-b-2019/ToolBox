import json
#Her importerer jeg Pythons json-modul

with open('hej.json', 'r', encoding="utf-8") as f:
	#Her åbner jeg den json-fil jeg gerne vil åbne. Den skal ligge i samme mappe som scriptet der skal åbne den. 'r' betyder at jeg åbner filen til at læse, og encoding="utf-8" er for at åbne filen med den generelle encoding standard
	liste_med_json = json.load(f)
	#Her oprettes en liste der indeholder alle json-objekter fra filen, som dictionaries.
	f.close()
	#Husk at luk filen


print(liste_med_json[2]["name"])
#Her er et eksempel på at bruge data fra listen. Der printes fra objekt nummer 3 (0 tælles med) i listen, og det objekts "name"-værdi.
