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

'''
Exercice 6: Ecrire un programme en langage Python qui demande
à l’utilisateur de saisir son âge et de lui afficher le message
« vous êtes Majeur ! » si l’âge tapé est supérieur ou égale à 18
et le message « vous êtes mineur ! » si l’âge tapé est inférieur à 18
'''
def major():
    age = float(input("type your age: "))
    print("you are ", end='')
    print("major" if age >= 18 else "not major")

'''
Exercice 7: Ecrire un programme en Python qui demande à l’utilisateur
de saisir 3 nombre x, y et z et de lui afficher leur maximum
'''
def max_of_three():
    first_number = float(input("type the first number: "))
    second_number = float(input("type the second number: "))
    third_number = float(input("type the third number: "))
    print("max is ", max(first_number, second_number, third_number))

'''
Exercice 8: Ecrire un programme en Python qui demande à l’utilisateur
de saisir un nombre entier n et de lui afficher
la valeur de la somme 1 + 2 + … + n =
'''
def reccurent_sum():
    number = float(input("type a number: "))
    final_sum = 0
    for n in range(1, number+1):
        final_sum += n
    print("sum is " + final_sum)