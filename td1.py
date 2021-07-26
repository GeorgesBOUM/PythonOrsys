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