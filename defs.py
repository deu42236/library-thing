import csv

#add books
def addBook(name, author, ISBN, availability):
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writeheader()
#add users
def addUser(usernameName, password, bookBorrowedISBN):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([usernameName, password, bookBorrowedISBN])
#remove users
def removeUser(username):
    with open('users.csv', 'rb') as file:
        writer = csv.writer(file)
        for row in csv.reader(file):
            if row[0] != username:
                writer.writerow(row)

#search csv
def searchCSV(filename, search):
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if search in row:
                return row



#login
def login(inp1=input("Enter your username: ")):
    if searchCSV("users.csv", inp1) != None or inp1 == "admin":
        inp2 = input("Enter your password: ")
        if inp1 == "admin" and inp2 == "admin":
            print("Welcome admin!")
            return "admin"
        elif searchCSV("users.csv", inp1)[1] == inp2:
            return inp1
    else:
        if input("User not found. Would you like to create an account? (y/n): ") == "y":
            addUser(input("Enter your username: "), input("Enter your password: "), None,)
            return login()
        



