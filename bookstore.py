print("!-----------------Welcome To Anant Book Store---------------------!")
import mysql.connector
mydb=mysql.connector.connect (host="localhost", user="root", password="vin07@SIN")

#CREATING DATABASE AND TABLE
mycursor=mydb.cursor()
mycursor.execute("create database if not exists store")
mycursor.execute("use store")
mycursor.execute("create table if not exists signup(username varchar(20),password varchar(20))")

while True:
    print("""1:Signup
2:Login""")

    ch=int(input("SIGNUP/LOGIN(1,2):"))

#SIGNUP
    if ch==1:

        username=input("USERNAME:")
        pw=input("PASSWORD:")

        mycursor.execute("insert into signup values('"+username+"','"+pw+"')")
        mydb.commit()

#LOGIN
    elif ch==2:

        username=input("USERNAME:")

        mycursor.execute("select username from signup where username='"+username+"'")
        pot=mycursor.fetchone()

        if pot is not None:
            print("VALID USERNAME!!!!!!")

            pw=input("PASSWORD:")

            mycursor.execute("select password from signup where password='"+pw+"'")
            a=mycursor.fetchone()

            if a is not None:
                print("""+++++++++++++++++++++++
+++LOGIN SUCCESSFULL+++
+++++++++++++++++++++++""")

                print("""======================================================================
++++++++++++++++++++++++++    MY BOOK STORE     +++++++++++++++++++++++++
==========================================================================""")

                mycursor.execute("create table if not exists Available_Books(BookName varchar(30) primary key,Genre varchar(20),Quantity int(3),Author varchar(20),Publication varchar(30),Price BIGINT)")
                mycursor.execute("create table if not exists Sell_rec(CustomerName varchar(20),PhoneNumber BIGINT unique key, BookName varchar(30),Quantity int(100),Price BIGINT,foreign key (BookName) references Available_Books(BookName))")
                mycursor.execute("create table if not exists Staff_details(Name varchar(30), Gender varchar(10),Age int(3), PhoneNumber BIGINT unique key , Address varchar(40))") 
                mydb.commit()

                while(True):
                    print("""1:Add Books
2:Search Books
3:Staff Details
4:Sell Record
5:Available Books
6:Total Income after the Latest Reset 
7:Exit""")

                    a=int(input("Enter your choice:"))

    #ADD BOOKS
                    if a==1:

                        print("All information prompted are mandatory to be filled")
                    
                        book=str(input("Enter Book Name:"))
                        genre=str(input("Genre:"))
                        quantity=int(input("Enter quantity:"))        
                        author=str(input("Enter author name:"))
                        publication=str(input("Enter publication house:"))
                        price=int(input("Enter the price:"))

                        mycursor.execute("select * from Available_Books where BookName='"+book+"'")
                        row=mycursor.fetchone()

                        if row is not None:
                            mycursor.execute("update Available_Books set quantity=quantity+'"+str(quantity)+"' where bookname='"+book+"'")
                            mydb.commit()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""")
                        
                        
                        else:
                            mycursor.execute("insert into Available_Books(BookName, Genre ,Quantity, Author, Publication,Price) values('"+book+"','"+genre+"','"+str(quantity)+"','"+author+"','"+publication+"','"+str(price)+"')")
                            mydb.commit()

                            print("""++++++++++++++++++++++
++SUCCESSFULLY ADDED++
++++++++++++++++++++++""") 
                   

                    elif a==2:

                        print("""1:Search by name
2:Search by genre
3:Search by author""")

                        l=int(input("Search by?:"))

        #BY BOOKNAME
                        if l==1:
                            olp=input("Enter Book to search:")

                            mycursor.execute("select * from available_books WHERE BookName='"+olp+"'")
                            tree=mycursor.fetchall()

                            if tree!=None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
                                print("BookName     Genre    Quantity    Author    Publication    Price")
                                mycursor.execute("select * from available_books WHERE genre='"+olp+"'")
                                for BookName, Genre ,Quantity, Author, Publication,Price in tree:
                                    print(f"{BookName}\t {Genre}\t {Quantity}\t {Author}\t{Publication}\t{Price}")

                            else:
                                print("BOOK IS NOT IN STOCK!!!!!!!")

        #BY GENRE
                        elif l==2:
                            g=input("Enter genre to search:")

                            mycursor.execute("select * from available_books where Genre='"+g+"'")
                            poll=mycursor.fetchall()

                            if poll!=None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
                                print("BookName     Genre    Quantity    Author    Publication    Price")
                                mycursor.execute("select * from available_books where genre='"+g+"'")
                                for BookName, Genre ,Quantity, Author, Publication,Price in poll:
                                    print(f"{BookName}\t {Genre}\t {Quantity}\t {Author}\t{Publication}\t{Price}")
                                

                            else:
                                print("BOOKS OF SUCH GENRE ARE NOT AVAILABLE!!!!!!!!!")


        #BY AUTHOR NAME
                        elif l==3:
                            au=input("Enter author to search:")

                            mycursor.execute("select * from available_books where author='"+au+"'")
                            home=mycursor.fetchall()

                            if home!=None:
                                print("""++++++++++++++++++++
++BOOK IS IN STOCK++
++++++++++++++++++++""")
                                print("BookName     Genre    Quantity    Author    Publication    Price")
                                mycursor.execute("select * from available_books where genre='"+au+"'")
                                for BookName, Genre ,Quantity, Author, Publication,Price in home:
                                    print(f"{BookName}\t {Genre}\t {Quantity}\t {Author}\t{Publication}\t{Price}")

                               

                            else:
                                print("BOOKS OF THIS AUTHOR ARE NOT AVAILABLE!!!!!!!")
                        

    #STAFF DETAILS
                    elif a==3:
                        print("1:New staff entry")
                        print("2:Remove staff")
                        print("3:Existing staff details")

                        ch=int(input("Enter your choice:"))

        #NEW STAFF ENTRY
                        if ch==1:
                            fname=input("Enter Fullname:")
                            gender=input("Gender(M/F/O):")
                            age=int(input("Age: "))
                            phno=int(input("Staff phone no.: "))
                            add=input("Address:")

                            s3=("insert into Staff_details(name,gender,age,phonenumber,address) values(%s,%s,%s,%s,%s)")
                            s4=(fname,gender,age,phno,add)
                            mycursor.execute(s3,s4)

                            print("""+++++++++++++++++++++++++++++
+STAFF IS SUCCESSFULLY ADDED+
+++++++++++++++++++++++++++++""")
                            mydb.commit()

        #REMOVE STAFF
                        elif ch==2:
                            nm=str(input("Enter staff name to remove:"))
                            mycursor.execute("select name from staff_details where name='"+nm+"'")
                            toy=mycursor.fetchone()

                            if toy is not None:
                                mycursor.execute("delete from staff_details where name='"+nm+"'")
                                print("""+++++++++++++++++++++++++++++++++
++STAFF IS SUCCESSFULLY REMOVED++
+++++++++++++++++++++++++++++++++""")
                                mydb.commit()

                            else:
                                print("STAFF DOESNOT EXIST!!!!!!")

        #EXISTING STAFF DETAILS
                        elif ch==3:
                            mycursor.execute("select * from Staff_details")
                            run=mycursor.fetchall()
                            tou=(['Name', 'Gender' ,'Age', 'PhoneNumber', 'Address'])
                            print("Name    gender    Age    PhoneNumber    Address    ",)
                            if run is not None:
                                for Name, Gender ,Age, PhoneNumber, Address in run:
                                    print(f"{Name}\t {Gender}\t {Age}\t {PhoneNumber}\t{Address}\t")
                            

                            else:
                                print("NO STAFF EXISTS!!!!!!!")
                            mydb.commit()

    #SELL HISTORY                                
                    elif a==4:
                        print("1:Sell history details")
                        print("2:Reset Sell history")

                        ty=int(input("Enter your choice:"))

                        if ty==1:
                            mycursor.execute("select * from sell_rec")
                            print("CustomerName    PhoneNumber    BookName    Quantity    Price ")
                            rt=mycursor.fetchall()
                            
                            for CustomerName ,PhoneNumber , BookName ,Quantity ,Price  in rt:
                                print(f"{CustomerName}\t {PhoneNumber}\t {BookName}\t {Quantity}\t{Price}")

                        if ty==2:
                            bb=input("Are you sure(Y/N):")

                            if bb=="Y":
                                mycursor.execute("delete from sell_rec")
                                mydb.commit()

                            elif bb=="N":
                                pass

    #AVAILABLE BOOKS
                    elif a==5:
                        mycursor.execute("select * from available_books order by bookname")
                        pt=mycursor.fetchall()
                        print("BookName     Genre    Quantity    Author    Publication    Price")
                        for BookName, Genre ,Quantity, Author, Publication,Price in pt:
                            print(f"{BookName}\t {Genre}\t {Quantity}\t {Author}\t{Publication}\t{Price}")

    #TOTAL INCOME AFTER LATEST UPDATE
                    elif a==6:
                        mycursor.execute("select sum(price) from sell_rec")
                        for x in mycursor:
                            print(x[0])
    #EXIT                    
                    elif a==7:
                        break

#LOGIN ELSE PART
            else:
                print("""++++++++++++++++++++++
++INCORRECT PASSWORD++
++++++++++++++++++++++""")


        else:
            print("""++++++++++++++++++++
++INVALID USERNAME++
++++++++++++++++++++""")

    else:
        break