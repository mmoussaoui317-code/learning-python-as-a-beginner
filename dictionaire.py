# creation of the first dectionnaire
stagiaire = {
    'nom': 'khalid',
    'prenom': 'yassir',
    'age': 17
}

# creation of this item if not exist or update it
stagiaire['note'] = 12.5

# update an item or change him value
stagiaire["age"] = 27

# delete an item from the dectionnaire by using the-key
del stagiaire['prenom']

# creation of the second dectionnaire
dectionaire1 = {
    # 'stagiaire': stagiaire,
    'ville': 'errachidia',
}

# use this method to update the dectionnaire
dectionaire1.update(stagiaire)

# function of printing
print(f'{stagiaire}')
print(f'{dectionaire1}')

# best method in by using the predifined methods
for key,value in stagiaire.items():
    print(f'{key} -- {value}')


# methode utilise by my self
for key in stagiaire:
    print(f'{key} +++ {stagiaire[key]}')
