#********************************************************************************************************
#                               P Y T H O N     P R O J E C T

#                                           LMS

# Author: Abd Khuffash
#********************************************************************************************************

import os
import re
from Library import Library
from Book import Book


def main():

    directory = "C:\\Users\\Abood\\PycharmProjects\\LMS\\"
    library = Library()

    library.loadfile("LMS.txt")
    library.DisplayBooks()


    print("""
*****************************
  __  __ ______ _   _ _    _ 
 |  \/  |  ____| \ | | |  | |
 | \  / | |__  |  \| | |  | |
 | |\/| |  __| | . ` | |  | |
 | |  | | |____| |\  | |__| |
 |_|  |_|______|_| \_|\____/ 
 
*****************************                           
    """)
    while 1 :

        print("""
            1. Adding new books to the library collection
            2. Searching for books within the library collection
            3. Editing the information of existing books
            4. Archiving books
            5. Removing books from the LMS
            6. Generating reports about the books available in the LMS
            7. Exit
            """)

        choice = input("Enter Your Choice: ")

        if choice == '1':
            c2=input("1.Add Book Manually\n2.Add Books From File\nYour Choice: ")

            if c2=='1':
                t=input("Title: ")
                p=input("Publisher: ")
                i10=input("ISBN-10: ")
                i13=input("ISBN-13: ")

                b2=Book(t,p,i10,i13,"")

                library.addBook(b2)

            elif c2=='2':
                file_name = input("File Name: ")
                file_path = os.path.join(directory, file_name)
                if file_name in os.listdir(directory):
                    print("The file exists.")

                    with open(file_name, "r") as file:
                        other_info = ""
                        for line in file:
                            try:
                                # print(line.strip())
                                if line.startswith("Title"):
                                    title = line.split(":", 1)[1].rstrip("\n").strip()
                                    # print(title)
                                elif line.startswith("Publisher"):
                                    publisher = line.split(":")[1].rstrip("\n").strip()
                                    # print(publisher)
                                elif line.startswith("ISBN-13"):
                                    isbn13 = line.split(":")[1].rstrip("\n").strip()
                                    # print(isbn13)
                                elif line.startswith("ISBN-10"):
                                    isbn10 = line.split(":")[1].rstrip("\n").strip()
                                    # print(isbn10)

                                elif re.match(r'^[a-zA-Z]', line):
                                    other_info += line

                                if line.startswith("\n"):
                                    # print(title)
                                    # print(publisher)
                                    # print(isbn10)
                                    # print(isbn13)
                                    # print(other_info)

                                    book = Book(title, publisher, isbn10, isbn13, other_info)
                                    book.info()
                                    library.addBook(book)

                                    other_info = ""
                                    title = ""
                                    publisher = ""
                                    isbn10 = ""
                                    isbn13 = ""

                            except ValueError:
                                print("Wrong Data Format")

                else:
                    print("The file does not exist.")

        elif choice == '2':
            #library.DisplayBooks()
            c=input("Enter a data to search About: ")
            found=library.search(c)

            if len(found)==0:
                print("The Data you Entered has no match!")
            else:
                for bk in found:
                    bk.info()
                cc = input("Do You Want to save the Result in WishList File?(y/n)")

                if cc.lower() == 'y':
                    f = open("Wishlist.txt", "w")

                    for bk in found:
                        f.write("Title: " + bk.title + "\n")
                        f.write("Publisher: " + bk.publisher + "\n")
                        f.write("ISBN-10: " + bk.isbn_10 + "\n")
                        f.write("ISBN-13: " + bk.isbn_13 + "\n")
                        f.write(bk.otherinfo)

        elif choice=='3':
            c=input("1.Edit by ISBNs\n2.Edit book from file\nYour Choice: ")

            if c=='1':
                isbn=input("Enter ISBN-10 for a book to edit: ")
                found=library.search(isbn)
                if len(found)==0:
                    print("No Such Book!")
                else:
                    print("BOOK INFO: ")
                    library.removefromLMS(isbn)

                    found[0].info()
                    print("If you Want to keep the parameter as it is press enter space to the specified parameter!")

                    title=input("Enter New Book Details\nTitle: ")
                    if not title:
                        title=found[0].title

                    publisher=input("Publisher: ")
                    if not publisher :
                        publisher=found[0].publisher

                    isbn10=input("ISBN-10: ")

                    if not isbn10:
                        isbn10=found[0].isbn_10

                    isbn13=input("ISBN-13: ")
                    if not isbn13:
                        isbn13=found[0].isbn_13

                    ncopies=input("Number of Copies: ")
                    if not ncopies:
                        ncopies=found[0].n_copies
                    other_info=input("Any Other Information(Enter ALL INFORMATION IF NOT WANTED TO BE EDITED):")
                    book=Book(title,publisher,isbn10,isbn13,other_info,ncopies)

                    library.addBook(book)
            elif c=='2':
                b5=[]
                file_name = input("File Name: ")
                file_path = os.path.join(directory, file_name)
                if file_name in os.listdir(directory):
                    print("The file exists.")

                    with open(file_name, "r") as file:
                        o = ""
                        for lline in file:
                            try:
                                print(lline.strip())
                                if lline.startswith("Title"):
                                    t1 = lline.split(":", 1)[1].rstrip("\n").strip()
                                    # print(title)
                                elif lline.startswith("Publisher"):
                                    p1 = lline.split(":")[1].rstrip("\n").strip()
                                    # print(publisher)
                                elif lline.startswith("ISBN-13"):
                                    isbn3 = lline.split(":")[1].rstrip("\n").strip()
                                    # print(isbn13)
                                elif lline.startswith("ISBN-10"):
                                    isbn0 = lline.split(":")[1].rstrip("\n").strip()
                                    # print(isbn10)

                                elif re.match(r'^[a-zA-Z]', lline):
                                    o += lline

                                if lline.startswith("\n"):
                                    #print(t1)
                                    #print(p1)
                                    #print(isbn0)
                                    #print(isbn3)
                                    #print(o)

                                    b7 = Book(t1, p1, isbn0, isbn3, o)
                                    # book.info()
                                    b7.info()
                                    b5.append(b7)

                                    o = ""
                                    t1 = ""
                                    p1 = ""
                                    isbn0 = ""
                                    isbn3 = ""

                            except ValueError:
                                print("Wrong Data Format")

                        for bk in b5:
                            bk.info()

                        isbn = input("Enter ISBN for a book from a file loaded: ")
                        found = []
                        for bk in b5:
                            if isbn == bk.isbn_10:
                                found.append(bk)

                        if len(found) == 0:
                            print("You entered ISBN For another BOOk that doesnot Exist in the file u specified!")
                        else:
                            b5.remove(found[0])
                            found[0].info()
                            print(
                                "If you Want to keep the parameter as it is press enter space to the specified parameter!")

                            title = input("Enter New Book Details\nTitle: ")
                            if not title:
                                title = found[0].title

                            publisher = input("Publisher: ")
                            if not publisher:
                                publisher = found[0].publisher

                            isbn10 = input("ISBN-10: ")

                            if not isbn10:
                                isbn10 = found[0].isbn_10

                            isbn13 = input("ISBN-13: ")
                            if not isbn13:
                                isbn13 = found[0].isbn_13

                            ncopies = input("Number of Copies: ")
                            if not ncopies:
                                ncopies = found[0].n_copies

                            other_info = input("Any Other Information(Enter ALL INFORMATION IF NOT WANTED TO BE EDITED):")
                            if not other_info:
                                other_info=found[0].otherinfo

                            b2 = Book(title, publisher, isbn10, isbn13, other_info, ncopies)
                            b5.append(b2)

                            c4 = input("1.Add NEWLY edited book to LMS\n2.Edit File Only\n Your Choice: ")

                            if c4 == '1':
                                c14 = input("FOR CONFIRMATION ENTER 'Y'")
                                if c14.lower() == 'y':
                                    library.addBook(b2)
                            elif c4 == '2':
                                c14 = input("FOR CONFIRMATION ENTER 'Y'")
                                if c14.lower() == 'y':
                                    f = open(file_name, "w")
                                    for bk in b5:
                                        f.write("\nTitle: " + bk.title + "\n")
                                        f.write("Publisher: " + bk.publisher + "\n")
                                        f.write("ISBN-10: " + bk.isbn_10 + "\n")
                                        f.write("ISBN-13: " + bk.isbn_13 + "\n")
                                        f.write(bk.otherinfo+"\n")
                                    f.close()


                    file.close()


                else:
                    print("The file does not exist.")

        elif choice == '4':

            iss=input("Enter ISBN To Achive: ")
            library.archive(iss)

        elif choice == '5':
            iss = input("Enter ISBN To Delete: ")
            library.deletefromarch(iss)




        elif choice=='6':
            library.report()


        elif choice=='7':
            library.exiting()
            exit(1)




        else:
            print("Invalid option!")






if __name__ == "__main__":
    main()