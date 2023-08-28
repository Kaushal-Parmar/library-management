class library:
    def __init__(self, listofbooks):
        self.books = listofbooks

    def displayavailablebooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print("->"+book)

    def borrowbook(self, bookname):
        if bookname in self.books:
            print(
                f"You have been issued {bookname}. please keep it safe and return it within 30 day")
            self.books.remove(bookname)
            return True
        else:
            print("Sorry, This book is either not avalaible or  has already bee issued to someone else.Please wait until the book is avalaible")
            return False

    def returnbook(self, bookname):
        self.books.append(bookname)
        print("Thanks for returning this book!")


class student:
    def requestbook(self):
        self.book = input("Enter the name of the you want to borrow: ")
        return self.book

    def returntbook(self):
        self.book = input("Enter the name of the you want to return: ")
        return self.book


if __name__ == "__main__":
    centralibrary = library(["JAVA", "PYHTON", "DJANGO", "PHP", "ANDROID"])
    # centralibrary.displayavailablebooks()
    student = student()
    while(True):
        welcomemsg = '''
        ------ WELCOME TO CENTRA LIBRARY ------

        Please choose an option:
            1. List all the books
            2. Request a book
            3. Add/Return a book
            4. Exit the library
        '''
        print(welcomemsg)
        a = int(input("Enter a choice "))
        if a == 1:
            centralibrary.displayavailablebooks()
        elif a == 2:
            centralibrary.borrowbook(student.requestbook())
        elif a == 3:
            centralibrary.returnbook(student.returntbook())
        elif a == 4:
            print("Thanks for using this library.....")
            exit()
        else:
            print("Invalid choice!")
