import defs


user = defs.login()
print(f"Hello {user}!")
if user == "admin":
    print("Choose action: 1. Add user 2. Remove user 3. Add book 4. Remove book 5. Exit")
    action = input("Enter action number: ")
    if action == "1":
        defs.addUser(input("Enter username: "), input("Enter password: "), None)
    elif action == "2": 
        print("not implemented yet")#remove user
        defs.removeUser(input("Enter username of the user: "))


    elif action == "3":
        defs.addBook(input("Enter book name: "), input("Enter author: "), input("Enter ISBN: "), True)
    elif action == "4":
        print("not implemented yet")#remove book
    elif action == "5":
        exit()