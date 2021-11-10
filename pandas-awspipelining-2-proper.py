import boto3
import pandas as pd
import sqlalchemy
import configparser

name = 'root'
password = 'Lifeiskind1'
database_name = 'city'

config_obj = configparser.ConfigParser()
config_obj.read(r"C:\Users\Jeffrey\Desktop\notes\mysqldb_aws_config.ini")
dbc = config_obj['aws']

aws_acc_key = dbc['aws_access_key_id']
aws_sec_key = dbc['aws_secret_access_key']
reg_na = dbc['region_name']

# this allows us to create engine
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)
f=pd.read_excel("",sheet_name=0)
client = boto3.client('s3', aws_access_key_id = aws_acc_key, aws_secret_access_key = aws_sec_key, region_name = reg_na)
path = 's3://bucketofmine17623/vehicle_income_expense_master.csv'

df = pd.read_csv(path, names=['inc_exp_id', 'inc_exp_desc', 'amount_sign', 'inc_exp_type'])
print(df)
print("------------------------------------------------------------")
df.to_sql(name='vehicle_income_expense_master_table', con=engine, if_exists='append', index=False)

df_q = pd.read_sql_query("select * from vehicle_income_expense_master_table;", engine)
print(df_q)

