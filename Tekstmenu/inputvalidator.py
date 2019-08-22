def getValidatedInput(besked, muligheder):
    """Denne funktion modtager en introduktion, en besked og en liste af muligheder."""
    intro = 'Mulighederne er:\n'
    for m in muligheder:
        intro = intro + m + ' '
    intro = intro + '\n'
    ind = input(intro + besked + ' ')
    if ind not in muligheder:
        ind = getValidatedInput(besked, muligheder)
    return ind

if __name__== '__main__':
    print(getValidatedInput('Vælg en', ['A', 'B', 'C']))
