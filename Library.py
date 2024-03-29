import os
import re

from Book import Book


class Library:
    def __init__(self):
        self.books = []
        self.arc = []



    def DisplayBooks(self):
        for b in self.books:
            b.info()


    def addBook(self,book):
        #book.info()
        for bk in self.books:
            if bk.isbn_10== book.isbn_10 and bk.isbn_13 == book.isbn_13:
                bk.n_copies=int(bk.n_copies)+1

                return
        self.books.append(book)

    def search(self,p):
        found=[]

        for b in self.books:
            if p.lower() == b.title.lower() or p.lower() == b.publisher.lower() or p == b.isbn_10 or p == b.isbn_13 :
                found.append(b)
            if p in b.otherinfo:
                found.append(b)

        return  found

    def removefromLMS(self,p):
        for b in self.books:
            if p == b.isbn_10:
                self.books.remove(b)


    def archive(self,p):

        for b in self.books:
            if p == b.isbn_10:
                b.info()
                if b.n_copies==1:
                    self.books.remove(b)
                    self.arc.append(b)
                else:
                    n=input("Print The number Of copies to Archive: ")
                    if int(n)== b.n_copies:

                        c20=input(f"Enter 'y' For Confirmation:NOTE {p}  WILL BE REMOVED FROM LMS ")
                        if c20.lower() =='y':
                            self.arc.append(b)
                            self.books.remove(b)
                            print("Added To Archive Successfully!")
                    elif int(n)> b.n_copies:
                        print("Can not Archive more that the copies!")
                    elif int(n)< b.n_copies:
                        temp=b.n_copies-int(n)
                        b.n_copies=int(n)
                        self.arc.append(b)
                        b.n_copies=temp
                        c20=input("Enter 'y' For Confirmation: ")
                        if c20.lower() =='y':
                            print("Added To Archive Successfully!")


    def deletefromarch(self,p):
        print("Archived Books: ")


        for b in self.arc:
            if b.isbn_10==p:
                b.info()
                c69=input("Enter 'y' For Confirmation of Deletion: ")
                if c69.lower()=='y':
                    self.arc.remove(b)
                    print("Removed Successfuly from Archive")

    def report(self):
        sum=0;

        for bk in self.books:
            sum+= int(bk.n_copies)

        print("\nThe Number Of Books in LMS: ",sum)
        print("\nThe Number Of Different books in LMS: ", len(self.books))

        sum=0
        for b in self.arc:
            sum+=int(b.n_copies)

        print("\nThe Number of Archived books: ", sum)

        pattern = r"Year\s*:\s*(\d{4})"

        year=input("Enter A Year : ")
        years=[]
        counter=0
        for bk in self.books:
            match = re.search(pattern, bk.otherinfo)
            if match:
                years.append(bk)
                y=match.group(1)
                if int(year) < int(y) :
                    counter+=1
                    #bk.info()

        print(f"The Number OF Books Newer Than the Year {year} are : ",counter)

        publishercount={}

        for bk in self.books:
            if bk.publisher in publishercount:
                publishercount[bk.publisher]+=bk.num_copies
            else:
                publishercount[bk.publisher]=bk.n_copies
        print("\nBook Distrubution By publisher: ")
        for p , c in publishercount.items():
            print(p+ ":",c)

        #############NO TIME #########
        yearcount={}
        for bk in self.books:
            match=re.search(pattern,bk.otherinfo)
            if match:
                y2=match.group(1)
                #print(y2)
                if y2 in yearcount:
                    yearcount[y2]+=bk.n_copies
                else:
                    yearcount[y2]=bk.n_copies
        print("\nBook Distrubution By year: ")

        for p , c in yearcount.items():
            print(p + ":" , c)





    def exiting(self):
        f=open("LMS.txt","w")

        for bk in self.books:
            f.write(f"Title:  {bk.title} \n")
            f.write(f"Publisher: {bk.publisher}\n")
            f.write(f"ISBN-10: {bk.isbn_10} \n")
            f.write(f"ISBN-13: {bk.isbn_13}\n")
            f.write(f"Number Of Copies: {bk.n_copies}\n")
            f.write(bk.otherinfo+"\n")




    def loadfile(self, filename):

        with open(filename, "r") as file:
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
                    elif line.startswith("Number Of Copies"):
                        no=line.split(":")[1].rstrip("\n").strip()

                    elif re.match(r'^[a-zA-Z]', line):
                        other_info += line

                    if line.startswith("\n"):
                        # print(title)
                        # print(publisher)
                        # print(isbn10)
                        # print(isbn13)
                        # print(other_info)

                        book = Book(title, publisher, isbn10, isbn13, other_info,no)
                        # book.info()
                        self.books.append(book)

                        other_info = ""
                        title = ""
                        publisher = ""
                        isbn10 = ""
                        isbn13 = ""
                        no=0

                except ValueError:
                    print("Wrong Data Format")
        file.close()

        print("Data Loaded Succesfully!")

