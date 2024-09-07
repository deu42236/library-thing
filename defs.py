import csv

#add books
def addBook(name, author, ISBN, availability):
    with open('books.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, author, ISBN, availability])
#add users
def addUser(usernameName, password, bookBorrowedISBN):
    with open('users.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([usernameName, password, bookBorrowedISBN])

#remove user
def removeUser(username):
    with open('users.csv', 'r', newline='') as file:
        rows = list(csv.reader(file))
    rows = [row for row in rows if row[0] != username]
    with open('users.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

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
            print("Incorrect password.")
            return login()
    else:
        print("User not found.")
        print("Please contact the admin to create an account.")
        return login()
        """

        
        uncomment this so users can create an account
        if input("User not found. Would you like to create an account? (y/n): ") == "y":
            addUser(input("Enter your username: "), input("Enter your password: "), None,)
            return login()
        """
