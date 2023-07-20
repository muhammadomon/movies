import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
from register_data import conn, add_data, update
from movies import search_movie
            
# Email configuration
def send_mail(gmail, code):
    sender_email = 'muhammadomon1212@gmail.com'
    reciever_email = gmail
    subject = 'Account activation'
    message = f'Your activation code is: {code}'
    # SMTP server configuration for gmail
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'muhammadomon1212@gmail.com'
    smtp_password = 'aeikuucdyvzvjklx'
    # Create a multipart message and set headers
    email_message = MIMEMultipart()
    email_message['From'] = sender_email
    email_message['To'] = reciever_email
    email_message['Subject'] = subject
    email_message.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(email_message)
#Generate code
def generate_code():
    s=''
    for i in range(4):
        s+=str(random.randint(0, 9))
    return s

#databasega yozish



#databasedan login va parolni tekshirish
def check_username_password(username:str, password:str):
    connect=conn()
    cur=connect.cursor()
    cur.execute("""
        select * from user
    """)
    rows = cur.fetchall()
    arr=[]
    for row in rows:
        arr.append(row)
    b=0
    for i in arr:
        if i[2]==username and i[3]==password:
            b=1

    return b


##databasedan login tekshirish
def check_username(username:str):
    conect=conn()
    cur=conect.cursor()
    cur.execute("""
        select * from user
    """)
    rows = cur.fetchall()
    arr=[]
    for row in rows:
        arr.append(row)
    b=0
    for i in arr:
        if i[2]==username:
            b=1

    return b



##Gmail tekshirish
def check_email(email:str):
    a=0
    if '@' in email and '.' in email and email[-1]!='.':
        a=1
    return a

#parol tekshirish
def check_password(password):
    p=0
    if len(password)<8:
        p=1
    return p


#asosiy
def login():
    print("1. Ro'yhatdan o'tish.  2.Kirish.")
    n=int(input("Tanlang: "))
    if n==1:
        first_name=input("Ismingiz: ")
        last_name=input("Familyangiz: ")
        username=input("Yangi login: ")

        l=check_username(username)
     
        if l==1:
            m=False

            while m!=True:
                username=input("Bunday login mavjud. Boshqa kiriting: ")
                l=check_username(username)
                if l==0:
                    m=True

        password=input("Parol(8tadan ko'p belgi bo'lsin): ")
        p=check_password(password)

        if p==1:
            w=False

            while w!=True:
                password=input("Parol noto'g'ri! 8tadan ko'p belgi bo'lsin: ")
                p=check_password(password)
                if p==0:
                    w=True
            
        email=input("Gmailingizni kiriting: ")
        a=check_email(email)

        while a==0:
            email=input("Email da xato, qayta kiriting: ")
            a=check_email(email)

        code=generate_code()

        send_mail(email, code)

        code2=input("Gmailingizga borgan habarni kiriting: ")
        x=False
        while x!=True:
            if code!=code2:
                code2=input("Xato! Qayta kiriting: ")
            elif code==code2:
                x=True

        dic={
            "first_name" : first_name,
            "last_name" : last_name,
            "username" : username,
            "password" : password,
            "email" : email,
            "is_active" : x,
            "like" : '',
            "dislike" : '',
            "history" : ''
            }
        add_data(dic, 'user')
        print("Muvaffaqiyatli ro'yhatdan o'ttingiz!")
        login()
    username=input("Login kiriting: ")
    password=input("Parol kiriting: ")
    check=check_username_password(username, password)
    if check==1:
        movie=search_movie()
        print(movie)
        l_or_d=input("Ushbu filmga like bosish->l, Dislike->d: ")
        if l_or_d.isupper()=='l':
            print('Like uchun tashakkur!')
            update('user', 'like', movie['id'], username)


    elif check==0:
        print("Login yoki parol xato!")
        yes_or_no=input("Qayta kiritasizmi?(Ha->y, Yo'q->n): ")
        if yes_or_no.lower()=='y':
            login()
        elif yes_or_no.lower()=='n':
            yes_or_no=input("Siz ro'yhatdan o'tvoqchimisiz?(Ha->y, Yo'q->n): ")
            if yes_or_no.lower()=='y':
                first_name=input("Ismingiz: ")
                last_name=input("Familyangiz: ")
                username=input("Yangi login: ")

                l=check_username(username)

                if l==1:
                    m=False

                    while m!=True:
                        username=input("Bunday login mavjud. Boshqa kiriting: ")
                        l=check_username(username)
                        if l==0:
                            m=True

                password=input("Parol(8tadan ko'p belgi bo'lsin): ")
                p=check_password(password)

                if p==1:
                    w=False

                    while w!=True:
                        password=input("Parol noto'g'ri! 8tadan ko'p belgi bo'lsin: ")
                        p=check_password(password)
                        if p==0:
                            w=True

                email=input("Gmailingizni kiriting: ")
                a=check_email(email)

                while a==0:
                    email=input("Email da xato, qayta kiriting: ")
                    a=check_email(email)

                code=generate_code()

                send_mail(email, code)

                code2=input("Gmailingizga borgan habarni kiriting: ")
                x=False
                while x!=True:
                    if code!=code2:
                        code2=input("Xato! Qayta kiriting: ")
                    elif code==code2:
                        x=True

                dic={
                    "first_name" : first_name,
                    "last_name" : last_name,
                    "username" : username,
                    "password" : password,
                    "email" : email,
                    "is_active" : x,
                    "like" : '',
                    "dislike" : '',
                    "history" : ''
                    }
                add_data(dic, 'user')
                print("Muvaffaqiyatli ro'yhatdan o'ttingiz!")
            login()


login()

