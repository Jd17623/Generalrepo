import admin_login as al
# import boto3
import pandas as pd
import validation
import user_login
# import mysql.connector
# import sqlalchemy
from datetime import date

# s3_client=boto3.client('s3', aws_access_key_id = '', aws_secret_access_key = '', region_name = '')
# file = s3_client.get_object(Bucket='',Key='')
ad = pd.read_csv(file['Body'], names = ['admin_id', 'admin_password'])
# # print(ad)
ad_user_id = ad.iloc[0, 0]
ad_password = ad.iloc[0, 1]
# print(ad_user_id)
# print(ad_password)

name = ''
password = ''
database_name = ''
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)

conn = mysql.connector.connect(user='', database='',
                               password='',
                               host="",
                               port=3306)
cursor = conn.cursor()

print("Types of login")
print("Select 1 for Admin login")
print("Select 2 for User login")
print("Select 3 to exit application")
user_input = int(input("Enter your choice: "))
if (user_input == 1):
    print("*** Welcome to Admin Login ***")
    admin_id = input("Enter Admin User id :")
    admin_password = input("Enter password :")
    if (admin_id == ad_user_id):
        if (admin_password == ad_password):
            print("--- Login Successful ---")
            while True:
                print("-----------------------------------------")
                print("Mainmenu")
                print()
                print("1. To Create a New User")
                print("2. To view a User")
                print("3. To view details of every Users")
                print("4. To Delete a User")
                print("5. To Delete all User Data")
                print("6. To Deactivate status of a User")
                print("7. To Deactivate status of all Users")
                print("8. To Reactivate status of a User")
                print("9. To Reactivate status of all Users")
                print("-----------------------------------------")
                admin_input = int(input("Enter your choice: "))
                if (admin_input == 1):
                    al.create()

                elif (admin_input == 2):
                    al.view()

                elif (admin_input == 3):
                    al.view_all()

                elif (admin_input == 4):
                    al.delete_one()

                elif (admin_input == 5):
                    al.delete_all()

                elif (admin_input == 6):
                    al.deactivate_one()

                elif (admin_input == 7):
                    al.deactivate_all()

                elif (admin_input == 8):
                    al.reactivate_one()

                elif (admin_input == 9):
                    al.reactivate_all()

                else:
                    print("#* Invalid Operation *#")

                contin = input("Do you want to Continue (y/n): ")

                if (contin == 'y'):
                    continue
                elif(contin == 'n'):
                    break
                else:
                    print("Please give valid action")

        else:
            print("!!!! Invalid Password !!!!")

    else:
        print("!!!! Invalid Admin Id !!!!")

elif (user_input == 2):
    print("*** Welcome to User Login ***")
    # user_id = int(input("Enter the User_id:"))
    if(validation.valid_user()):
        passwd = input("Enter password: ")
        see_all = pd.read_sql_query("select * from User_Details;", engine)
        d = (date.today() - see_all['Date'][0]).days
        if (len(passwd) == 6):
            if (d <= 3):
                user_login.new_password()

        elif(len(passwd) >= 8):
            user_login.regular_login()

        else:
            print("Length of the Password is not Correct")








