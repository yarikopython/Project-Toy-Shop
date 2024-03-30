from termcolor import colored
import os
from tools_for_csv import write, reader, updater
from database import delete_toy, create_toy, get_toy, update_toy, session_local, toys


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
        print("---------------------------")
        match inputik:
            case 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                data = []
                try:
                    print("List of Toys:")
                    
                    input1 = str(input("Name: "))
                    input2 = float(input("Price: "))
                    input3 = str(input("Category: "))
                    input4 = int(input("Amount: "))
                    create_toy(input1, input2, input3, input4)
                    for add in (input1, input2, input3, input4):
                        data.append(add)
                    write("csv.csv", data)
                except TypeError:
                    print("False Type")
                finally:
                    os.system('cls' if os.name == 'nt' else 'clear')
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
                    name = input("Name: ")
                    delete_toy(name)
                except TypeError:
                    print("False Type")
                finally:
                   os.system('cls' if os.name == 'nt' else 'clear') 
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("List of Toys:")
                reader("csv.csv")
                try:
                    idik = int(input("Id of Toy: "))
                    get_toy(idik)
                except TypeError:
                    print("False Type")
                finally:
                    os.system('cls' if os.name == 'nt' else 'clear')
            case 4:
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
                    inputs_list = []
                    print("List of Toys:")
                    reader("csv.csv")
                    id
                    name = input("Enter the name of the toy: ")
                    price = float(input("Enter the price of the toy: "))
                    category = input("Enter the category of the toy: ")
                    amount = int(input("Enter the amount of the toy: "))
                    for inputs in (name, price, category, amount):
                        inputs_list.append(inputs)
                    update_toy(id, inputs)
                except TypeError:
                    print("False Type")
                finally:
                    os.system('cls' if os.name == 'nt' else 'clear')   
            case 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
                os.system('cls' if os.name == 'nt' else 'clear')
menu()
