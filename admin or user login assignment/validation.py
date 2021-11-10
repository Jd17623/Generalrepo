import sqlalchemy
import pandas as pd

name = 'root'
password = 'Lifeiskind1'
database_name = 'city'
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)

def valid_user():
    # data = pd.read_sql_query("select * from User_Details where user_id='{}';".format(user_id), engine)
    # d = (date.today() - data['Date'][0]).days
    # print(d)
    global user_id
    user_id = input("Enter the User_id:")
    list1 = []
    see_all = pd.read_sql_query("select * from User_Details where status_mode = 'Active';", engine)
    for i in see_all['User_id']:
        list1.append(i)

    if (user_id not in list1):
        print("User does not Exist or is Deactivated")
        return False
    elif(user_id in list1):
        print("------------------------------------")
        print("This User is a Valid and Active user")
        print("------------------------------------")
        return True
    else:
        print("Invalid User Id")
        return False


# valid_user()