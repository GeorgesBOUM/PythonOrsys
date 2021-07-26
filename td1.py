'''
Exercice 1: Ecrire un programme en langage Python qui demande à l’utilisateur
de saisir son nom et de lui afficher son nom avec un message de bienvenue !
'''
def read_and_print_name():
    name = input("type your name: ")
    print("the name you typed is " + name)

'''
Exercice 2: Ecrire un programme en Python (une fonction) qui demande
à l’utilisateur de saisir deux nombres a et b et de lui afficher leur somme :
a + b (passage par argument)
'''
def sum_two_numbers():
    first_number = float(input("type the first number: "))
    second_number = float(input("type the second number: "))
    print(f"the sum of {first_number} and {second_number}\
    is {first_number + second_number}")

'''
Exercice 3: Ecrire un programme en Python qui demande à l’utilisateur de
saisir deux nombres a et b et de lui afficher leur maximum.
(sans utiliser la fonction max())
'''
def not_built_in_max():
    first_number = float(input("type the first number: "))
    second_number = float(input("type the second number: "))
    print(first_number if (first_number > second_number) else second_number)

'''
Exercice 4: Ecrire un programme en langage Python qui affiche
les 100 premiers nombres entiers
'''
def first_hundred_numbers():
    for i in range(100):
        print(i, end=',')
    
'''
Exercice 5: Ecrire un programme en langage Python qui demande
à l’utilisateur de saisir son nombre entier et de lui afficher
si ce nombre est pair ou impair
'''
def odd_number():
    number = float(input("type a number: "))
    print(f"{number} is ", end='')
    print("odd " if number % 2 != 0 else "not odd")
