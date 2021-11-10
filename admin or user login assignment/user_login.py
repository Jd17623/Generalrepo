import validation
import pandas as pd
import sqlalchemy
import mysql.connector

name = 'root'
password = 'Lifeiskind1'
database_name = 'city'
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)

conn = mysql.connector.connect(user='root', database='city',
                               password='Lifeiskind1',
                               host="localhost",
                               port=3306)
cursor = conn.cursor()


def new_password():
    while True:
        user_id = input("Enter the User_id:")
        new_passwd = input("Enter new password, (Must be more than 8 characters): ")
        if (len(new_passwd) >= 8):
            cursor.execute("update User_Details set Password=%s  where User_id=%s", (new_passwd, user_id))
            conn.commit()
            print("Password has been Updated")
            print("")
            break

        else:
            print("!!! Incorrect Password Length !!!")


def regular_login():
    list = []
    user_id = input("Enter the User_id:")
    # data=pd.read_sql_query("select * from User_Details where user_id='{}';".format(user_id), engine)
    see_all = pd.read_sql_query("select * from User_Details;", engine)
    for i in see_all['User_id']:
        list.append(i)

    if (user_id in list):
        reg_password = input("Enter the password: ")
        if (reg_password == str(see_all['Password'][0])):
            print("Login Successful")
            while True:
                print("-----------------------------------------")
                print("Mainmenu")
                print()
                print("1. View Users complete Details")
                print("2. View Users brief Details")
                print("3. Logout")
                user_input = int(input("Enter your choice: "))
                if (user_input == 1):
                    see_all = pd.read_sql_query("select * from User_Details where User_id={};".format(user_id), engine)
                    print(see_all)

                elif(user_input == 2):
                    see_less = pd.read_sql_query("select User_id, Password from User_Details where User_id={};".format(user_id), engine)
                    print(see_less)

                elif(user_input == 3):
                    print("Logged out")
                    break

                else:
                    print("Invalid operation")










