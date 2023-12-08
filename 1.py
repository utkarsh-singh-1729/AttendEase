# import math, random
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vin07@SIN", 
    database="bank"
)


# def generateOTP():
    
#     digits = "0123456789"
#     OTP = ""

    
#     for i in range(6):
#         OTP += digits[math.floor(random.random() * 10)]

#     return OTP





print("!---------------------------------------------------------------------!")
print("!        **************WELCOME TO HDFC Bank***************            !")
print("!---------------------------------------------------------------------!")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("create table if not exists account(account_number BIGINT PRIMARY KEY,account_holder VARCHAR(255) NOT NULL,balance BIGINT NOT NULL, mobile BIGINT NOT NULL)")
swl="select * from account" 
mycursor.execute(swl) 
rust=mycursor.fetchall()

ch=""
while ch!='N' or ch!='n':
    print("!---------------------------------------------------------------------!")
    print("!      Press 1 for Open A bank Account                                !")            
    print("!      Press 2 for Deposit Amount                                     !")            
    print("!      press 3 for Withdraw Amount                                    !")
    print("!      Press 4 for Balance Enquiry                                    !")
    print("!      Press 5 for  Display Customer Details                          !")
    print("!      Press 6 for Close An Account                                   !")            
    print("!---------------------------------------------------------------------!")
    c=int(input("Enter Your Choise : "))
    if c==1:
        account_holder=input("Enter Your Name : ").strip()
        mobile= int(input("Enter your Mobile Number : "))
        account_number= int(input("Enter Account Number : "))
        balance=int(input("Enter your intial balance : "))
        
        s1=("insert into account(account_number,account_holder,balance,mobile)values(%s,%s,%s,%s)")
        d1= (account_number,account_holder,balance,mobile)
        mycursor.execute(s1,d1)
        mydb.commit();
        print("!-------------------------------------------------------------------------------!")
        print("!******Account Created Successfully**********                                   !")
        print("!We will sent internet banking id & password to your ragister mobile            !")
        print("!-------------------------------------------------------------------------------!")
    if c==2:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        amt= int(input("Enter Amount : "))
        s2=(f"SELECT balance FROM account WHERE account_number={account_number}")
        mycursor.execute(s2)
        balance2 = mycursor.fetchone()
        new_balance= balance2[0]+amt
        s3=(f"UPDATE account SET balance = {new_balance} WHERE account_number = {account_number}")
        mycursor.execute(s3)
        print(f"Amount Deposited & New Balance is : ₹{new_balance}")

    if c==3:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        amt= int(input("Enter Amount : "))
        s2=(f"SELECT balance FROM account WHERE account_number={account_number}")
        mycursor.execute(s2)
        balance2 = mycursor.fetchone()
        vb=generateOTP()
        new_balance= balance2[0]-amt
        if (new_balance>=0):
            s3=(f"UPDATE account SET balance = {new_balance} WHERE account_number = {account_number}")
            mycursor.execute(s3)
            print(f"Amount withdraw successfully \n New Balance is : ₹{new_balance}")
        else:
            print("insufficient balance")
        # else:
        #     print("authentication problem")
    if c==4:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        s2=(f"SELECT balance FROM account WHERE account_number={account_number}")
        mycursor.execute(s2)
        balance2 = mycursor.fetchone()
        print("Your Account balance is : ₹",balance2[0])
    
    if c==5:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        s2=(f"SELECT * FROM account WHERE account_number={account_number}")
        mycursor.execute(s2)
        detail = mycursor.fetchone()
        for i in detail:
            print(f"{i}\n")
    if c==6:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        s4=(f"DELETE FROM account WHERE account_number={account_number}")
        mycursor.execute(s4)
        mydb.commit();
        print("We have received your request to close your account.\n We will close your account within 24 hours")
    