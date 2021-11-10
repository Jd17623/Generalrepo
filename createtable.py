import mysql.connector
user_ = input("Enter the user: ")
database_ = input("Enter the database: ")
password_ = input("Enter password: ")
host_ = input("Enter host: ")
port_ = input("Enter port: ")
try:
    conn = mysql.connector.connect(user = user_, database = database_, password = password_, host=host_, port=port_)

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                                 Id int(11) NOT NULL,
                                 Name varchar(250) NOT NULL,
                                 Price float NOT NULL,
                                 Purchase_date Date NOT NULL,
                                 PRIMARY KEY (Id)) """
    cursor = conn.cursor()
    result = cursor.execute(mySql_Create_Table_Query)

except:
    print("Table already exists")