# les dictionnaire

# creation de dictionnaire

personne = {
    "nom": "Jean",
    "age": 26,
    "ville": "paris"
}


# acceder aux valeurs
# first method
print(personne["nom"])
# second method
print(personne.get("age"))


#ajouter de valuers ou modifie

personne["adress"] = "rue 120"
print(personne.get("adress"))


# personne.append("cin", "EE458")
# print(personne["cin"])


# supprimier 

del personne["ville"]


# # parcourir 

# for cle, ":", val (
#     print(cle)

# )


# functions
# fun simple 
def say_hello():
    print("hello")


say_hello()



# fun with parameters
def salutation(nom):
    print(f"bonjour", {nom})

salutation("mark")

# fun avec return
def some(a, b):
    return a+ b

print(f"the some of the a and b: ", {some(14, 2)})

# fun with the defaiult paras
def persntation(nom, age=14): 
    print(f"hello Mr|Ms: {nom}, your age is: {age} years old!!")

persntation("ahemd") #take the default value of the params
persntation("saad", 25) #send to it the age to skip the default value