import mysql.connector
import pandas as pd
import configparser

config_obj = configparser.ConfigParser()
config_obj.read(r"C:\Users\Jeffrey\Desktop\notes\mysqldb_aws_config.ini")
dbc = config_obj['mysql']

user = dbc['user']
pwd = dbc['password']
ho = dbc['host']
db = dbc['db']

conn = mysql.connector.connect(user = user,
                               database = db,
                               password = pwd,
                               host=ho,
                               port=3306)

cursor = conn.cursor()
query = 'show tables;'
pdf = pd.read_sql(query, con = conn)

print(pdf)