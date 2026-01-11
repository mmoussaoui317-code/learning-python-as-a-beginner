# creation the jeu de devianette 

import random

# we are create an simple function and to get a number cachee 'secret'

def jeu_divinette():
    print('=== jeu divienette ===')
    print('divinez un nnomber enter 1 et 100')

    number_secret = random.randint(1, 100)
    tentatives = 0
    trouve = False

    while not trouve:
        try:
            devine = int(input('voutre predit : '))
            tentatives += 1
            if devine <= 100 and devine > 0:

                if devine < number_secret:
                    print('trop bas!!')
                elif devine > number_secret:
                    print('trop huat !!')
                else:
                    print(f'bravo! trouve en {tentatives} tentatives')
                    trouve = True
            else :
                raise ValueError("Must Respect the range Of Value Please !!")
        except ValueError:
            print("veuillez entre un nomber in between 1 - 100")
            rejouer = input('vouluez vous rejeur ? (oui | non) : ')
            if rejouer.lower() == 'oui':
                jeu_divinette()
            else:
                print('Goodby See You Latter')
            break
                












def calculate_the_numbers_total():
    n = int(input('Enter Number : '))
    some = 0
    for i in range(1, n +1):
        some += i

    return some

def calculate_the_pair():
    n = int(input('Enter Number : '))
    some = 0
    for i in range(1, n +1, 2):
        some += i

    return some

def affiche_numbers_in_one_ligne():
    n = int(input("Give Me Your Number : "))
    for num in range(n, 0, -1):
        print(f"{num}", end=" | ")


# cxooment

if __name__ == '__main__':
    jeu_divinette()
    # print(calculate_the_numbers_total())
    # print(calculate_the_pair())
    # affiche_numbers_in_one_ligne()



# jeu_divinette()