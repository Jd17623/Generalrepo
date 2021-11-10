import pandas as pd
import sqlalchemy

name = ''
password = ''
database_name = ''

# this allows us to create engine
engine = sqlalchemy.create_engine('mysql+pymysql://' + name + ':' + password + '@localhost:3306/' + database_name)
# engine = sqlalchemy.create_engine('mysql+pymysql://root:mahendrakn@1996@localhost:3306/etl')

# using engine we r reading the query to see contents of a table
df_q = pd.read_sql_query("select * from empdept;", engine)
print(df_q)

# this is used to create a table a new table based on the original or just append the data appropriatly if table already exists
df_q.to_sql(name='temp', con=engine, if_exists='append', index=False)

dfcsv = pd.read_csv(r"C:\Users\Jeffrey\Downloads\vehicle_master.csv")
print(dfcsv)
# dfcsv.to_sql(name='veh_mast', con=engine, if_exists='append', index=False)
