def save_books():
    file = open("books.txt", "w")
    for book in books:
        file.write(
            book["title"] + "," +
            book["author"] + "," +
            str(book["available"]) + "\n"
        )
    file.close()
    print("Books saved!")
books = []
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    book ={
    "title" : title,
    "author" : author,
    "available": True
}
    books.append(book)
    print("Book added successfully!")
def view_books():
    if len(books) == 0:
        print("No books found!")
        return

    for book in books:
            if book["available"] == True:
                status = "Available"
            else:
                status = "Borrowed"

            print("Title:", book["title"],
              "| Author:", book["author"],
              "| Status:", status
        )
def search_book():
    found = False
    title= input("Enter book Title: ")
    for book in books:
        if book["title"]==title:
            if book["available"] == True:
                status = "Available"
            else:
                status = "Borrowed"
            print("Title:", book["title"],
              "| Author:", book["author"],
              "| Status:", status
        )
            found = True
    if found ==False:
        print("Book not found! ")
def borrow_book():
    found = False
    title = input("Enter book title: ")
    for book in books:
        if book["title"]==title:
            found= True
            if book["available"]==True:
                book["available"]=False

                print("Book borrowed successfully!")
            else:
                print("Book is already borrowed!")
    if found == False:
        print("Book not found!") 
def return_book():
    found = False
    title = input("Enter book title: ")
    for book in books:
        if book["title"]==title:
            found= True
            if book["available"]==False:
                book["available"]=True

                print("Book returned successfully!")
            else:
                print("Book is already available!")
    if found == False:
        print("Book not found!")
def load_books():
    file = open("books.txt","r")
    for line in file:
        data=line.strip().split(",")
        book = {
        "title" : data[0],
        "author" : data[1],
        "available" : data[2] == "True"
    }
        books.append(book)
    file.close()
load_books()
while True:
    print("\n1. Add book")
    print("2. View books")
    print("3. Search book")
    print("4. Borrow book")
    print("5. Return book")
    print("6. Save books")
    print("7. Exit")

    choice = input("Enter choice")
    if choice == "1":
        add_book()
    elif choice == "2":
        view_books()
    elif choice == "3":
        search_book()
    elif choice == "4":
        borrow_book()
    elif choice == "5":
        return_book()
    elif choice == "6":
        save_books()
    elif choice == "7":
        print("Goodbye!")
        break