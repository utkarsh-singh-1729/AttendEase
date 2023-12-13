import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="vin07@SIN"
)


import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()



welf="WELCOME TO BLACK ROCK"
speak(welf)

print("!---------------------------------------------------------------------!")
print("!        **************WELCOME TO BLACK ROCK***************            !")
print("!---------------------------------------------------------------------!")
mycursor = mydb.cursor()
mycursor.execute("create database if not exists bank")
mycursor.execute("use bank")
mycursor.execute("create table if not exists account_d(account_number BIGINT AUTO_INCREMENT PRIMARY KEY,account_holder VARCHAR(255) NOT NULL,balance BIGINT NOT NULL, mobile BIGINT NOT NULL UNIQUE, email varchar(78),aadhaar bigint, pan varchar(20),address varchar(90))")
swl="select * from account_d" 
mycursor.execute(swl) 
rust=mycursor.fetchall()
if rust==[]:
    mycursor.execute("insert into account_d()values(591898868667,'Akarsh',98000,9795538809,'singh.akarsh98@gmail.com',786557654866,'SAIPS6678J','DHOOMANGANJ')")
    mydb.commit();

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
        mycursor = mydb.cursor()
        account_holder=input("Enter Your Name : ").strip()
        email=input("Enter your email: ")       
        aadhaar=input("Enter your aadhaar no: ")
        pan=input("Enter your pan no: ")
        address=input("Enter your address: ")
        mobile= int(input("Enter your Mobile Number : "))
        balance=int(input("Enter your intial balance : "))
        s1=("insert into account_d(account_number,account_holder,balance, mobile, email,aadhaar, pan,address)values(NULL,%s,%s,%s,%s,%s,%s,%s)")
        d1= (account_holder,balance,mobile,email,aadhaar, pan,address)
        mycursor.execute(s1,d1)
        mydb.commit();
        mycursor = mydb.cursor()
        sho=(f"SELECT account_number FROM account_d WHERE mobile={mobile}")
        mycursor.execute(sho)
        accoun = mycursor.fetchone()
        
        print(f"!--------------------------------------------------------------------------------!")
        print(f"!******dear {account_holder} your Account Created Successfully**********         !")
        print(f"!We will sent internet banking id & password to your ragister email              !")
        print(f"!your account number is :{accoun[0]}                                             !")
        print(f"!--------------------------------------------------------------------------------!")
        acy=(f"dear {account_holder} your Account Created Successfully your account number is :{accoun[0]}")
        speak(acy)
    if c==2:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        amt= int(input("Enter Amount : "))
        s2=(f"SELECT balance FROM account_d WHERE account_number={account_number}")
        mycursor.execute(s2)
        balance2 = mycursor.fetchone()
        new_balance= balance2[0]+amt
        s3=(f"UPDATE account_d SET balance = {new_balance} WHERE account_number = {account_number}")
        mycursor.execute(s3)
        DEP=(f"Amount Deposited & New Balance is : ₹{new_balance}")
        speak(DEP)
        print(DEP)

    if c==3:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        amt= int(input("Enter Amount : "))
        s2=(f"SELECT balance FROM account_d WHERE account_number={account_number}")
        mycursor.execute(s2)
        balance2 = mycursor.fetchone()
        # vb=generateOTP()
        new_balance= balance2[0]-amt
        if (new_balance>=0):
            s3=(f"UPDATE account_d SET balance = {new_balance} WHERE account_number = {account_number}")
            mycursor.execute(s3)
            WITHD=(f"Amount withdraw successfully \n New Balance is : ₹{new_balance}")
            print(WITHD)
            speak(WITHD)
        else:
            ewl=("insufficient balance")
            print(ewl)
            speak(ewl)
        # else:
        #     print("authentication problem")
    if c==4:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        s2=(f"SELECT balance FROM account_d WHERE account_number={account_number}")
        mycursor.execute(s2)
        balance2 = mycursor.fetchone()
        enqy=("Your Account balance is : ₹",balance2[0])
        print(enqy)
        speak(enqy)
    
    if c==5:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        s2=(f"SELECT * FROM account_d WHERE account_number={account_number}")
        mycursor.execute(s2)
        detail = mycursor.fetchone()
        for i in detail:
            print(f"{i}\n")
    if c==6:
        mycursor = mydb.cursor()
        account_number=int(input("Enter Account Number : "))
        s4=(f"DELETE FROM account_d WHERE account_number={account_number}")
        mycursor.execute(s4)
        mydb.commit();
        cls=("We have received your request to close your account. We will close your account within 24 hours")
        print(cls)
        speak(cls)
    