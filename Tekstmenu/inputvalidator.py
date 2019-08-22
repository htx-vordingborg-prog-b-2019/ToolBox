def getValidatedInput(besked, muligheder):
    """Denne funktion modtager en introduktion, en besked og en liste af muligheder.

    Parametre:
    besked - Besked til brugeren
    muligheder - Liste af mulige lovlige indtastninger"""

    intro = 'Mulighederne er:\n'
    # Byg en string af de mulige lovlige indtastninger
    for m in muligheder:
        intro = intro + m + ' '
    intro = intro + '\n'
    # Modtag input fra brugren
    ind = input(intro + besked + ' ')
    # Kontroller om indtastning er lovlig,
    # ellers kald denne funktion igen med samme parametre
    if ind not in muligheder:
        ind = getValidatedInput(besked, muligheder)
    return ind

if __name__== '__main__':
    print(getValidatedInput('Vælg en', ['A', 'B', 'C']))
