from termcolor import colored
import os
from csv_reader import write, csv_reader
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
                    data.append(input1)
                    data.append(input2)
                    data.append(input3)
                    data.append(input4)
                    write("csv.csv", data)
                except TypeError:
                    print("False Type")
                finally:
                    os.system('cls' if os.name == 'nt' else 'clear')
            case 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                try:
                    name = input("Name: ")
                    print(delete_toy(name))
                except TypeError:
                    print("False Type")
                finally:
                   os.system('cls' if os.name == 'nt' else 'clear') 
            case 3:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("List of Toys:")
                csv_reader("csv.csv")
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
                    print("List of Toys:")
                    csv_reader("csv.csv")
                    name = input("Enter the name of the toy: ")
                    price = float(input("Enter the price of the toy: "))
                    category = input("Enter the category of the toy: ")
                    amount = int(input("Enter the amount of the toy: "))
                    update_toy(name, price, category, amount)
                except TypeError:
                    print("False Type")
                finally:
                    os.system('cls' if os.name == 'nt' else 'clear')   
            case 5:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
                os.system('cls' if os.name == 'nt' else 'clear')
menu()
