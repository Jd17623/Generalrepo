from datetime import datetime
from random import randint
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

def create():
    print("For User Id we can use Mobile number or Email Id")
    newuser_id = input("Enter User Id: ")
    password = str(randint(100000, 999999))
    now = datetime.now()
    date = now.date()
    time = now.strftime('%H:%M:%S')

    # dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    status = "Active"
    print("date and time =", date, time)
    new_user = [newuser_id, password, date, time, status]

    df = pd.DataFrame([new_user], columns=['User_id', 'Password', 'Date', 'Time', 'status_mode'])
    df.to_sql(name="User_Details", con=engine, if_exists='append', index=False)
    print("User has been Created Successfully")


def view_all():
    see_all = pd.read_sql_query("select * from User_Details;", engine)
    print("Details of all Users: ")
    print(see_all)


def view():
    list1 = []
    see_all = pd.read_sql_query("select * from User_Details;", engine)
    # print(see_all)
    for i in see_all['User_id']:
        list1.append(i)
    print("->",list1)

    user_id = input("Enter the User_id:")
    print(user_id)
    if (user_id in list1):
        # user_detail = pd.read_sql_query("select * from User_Details where User_id={};".format(user_id), engine)
        user_detail = pd.read_sql_query(f"select * from User_Details where User_id= '{user_id}';", engine)
        print("Details of the Selected User:")
        print(user_detail)
    else:
        print("!!!! User does not exist !!!!")


def delete_all():
    cursor.execute("delete from User_Details")
    conn.commit()
    print("All User details have been succesfully Deleted")


def delete_one():
    list1 = []
    see_all = pd.read_sql_query("select * from User_Details;", engine)
    for i in see_all['User_id']:
        list1.append(i)

    user_id = input("Enter the User_id:")
    if (user_id in list1):
        cursor.execute(f"delete from User_Details where User_id= '{user_id}';")
        conn.commit()
        print("User details deleted succesfully")
    else:
        print("!!!! User does not exist !!!!")


def deactivate_one():
    list1 = []
    see_all = pd.read_sql_query("select * from User_Details;", engine)
    for i in see_all['User_id']:
        list1.append(i)

    user_id = input("Enter the user id :")
    if (user_id in list1):
        cursor.execute(f"update User_Details set status_mode= '{'Deactive'}' where User_id= '{user_id}';")
        conn.commit()
        print("User status is now Deactivated")
    else:
        print("!!!! User does not exist !!!!")


def deactivate_all():
    cursor.execute("update User_Details set status_mode='Deactive' ")
    conn.commit()

    print("All User status has been Deactivated")


def reactivate_one():
    list1 = []
    see_all = pd.read_sql_query("select * from User_Details;", engine)
    for i in see_all['User_id']:
        list1.append(i)

    user_id = input("Enter the user id :")
    if (user_id in list1):
        cursor.execute(f"update User_Details set status_mode= '{'Active'}' where User_id= '{user_id}';")
        conn.commit()
        print("User status is now Reactivated")


def reactivate_all():
    cursor.execute("update User_Details set status_mode='Active' ")
    conn.commit()

    print("All User status has been Reactivated")


