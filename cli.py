from termcolor import colored
from termcolor import COLORS
import os
from database import delete_toy, create_toy, get_toy, update_toy, session_local

def menu():
    while True:
        print("---------------------------")
        print("Welcome to Toy Shop")
        print(colored("\t [1] Create new Toys", "blue"))
        print(colored("\t [2] Delete Toys", "red"))
        print(colored("\t [3] Get information of Toys", "green"))
        print(colored("\t [4] Update Toy", "yellow"))
        print(colored("\t [5] Exit", "black"))
        inputik = int(input("What you will choose?: "))
        match inputik:
            case 1:
                input1 = input("Name: ")
                input2 = float(input("Price: "))
                input3 = input("Category: ")
                input4 = int(input("Amount: "))
                print(create_toy(input1, input2, input3, input4))
                os.system('cls' if os.name == 'nt' else 'clear')
            case 2:
                name = input("Name: ")
                print(delete_toy(name))
                os.system('cls' if os.name == 'nt' else 'clear')
            case 3:
                idik = int(input("Id of Toy: "))
                print(get_toy(idik))
                os.system('cls' if os.name == 'nt' else 'clear')
            case 4:
                name = input("Enter the name of the toy: ")
                price = float(input("Enter the price of the toy: "))
                category = input("Enter the category of the toy: ")
                amount = int(input("Enter the amount of the toy: "))
                print(update_toy(name, price, category, amount))
                os.system('cls' if os.name == 'nt' else 'clear')
            
            case 5:
                break