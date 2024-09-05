import csv
import defs


def login(inp1=input("Enter your username: ")):
    if defs.searchCSV("users.csv", inp1) != None:
        inp2 = input("Enter your password: ")
        if inp1 == "admin" and inp2 == "admin":
            print("Welcome admin!")
            return "admin"
        elif defs.searchCSV("users.csv", inp1)[1] == inp2:
            return inp1
login()












# def login(inp1 =input("Enter your username: "), inp2 = input("Enter your password: ")):

#     if inp1 == "admin" and inp2 == "admin":
#         print("Welcome admin!")
#         return "admin"
#     #admin login to add/remove books to do

#     #login system
#     elif searchCSV("users.csv", inp1) != None:
#         if searchCSV("users.csv", inp1)[1] == inp2:
#             return inp1
        