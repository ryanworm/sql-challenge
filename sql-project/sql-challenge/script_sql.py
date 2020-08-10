## *** importing dependancies *** ##
import psycopg2
import sys, os 
import numpy as numpy
import pandas as pandas
import cred_sql asd creds
import pandas.io.sql as psql

### *** Loading the PSQL Database *** ### 

# Setting up the connection to the server

conn_string = "host=" + creds.PGHOST +" port" + "5432" + " dbname=" + creds.PGDATABASE + " user=" + creds.PGUSER\
+ " password=" creds.PGPASSWORD
conn=psycopg2.connect(conn_string)
print("Connected")

### ** Create a cursor object ** ### 
cursor = conn.cursor()

def load_data(schema, table):

    sql_command = "SELECT * FROM {}.{};".format(str(schema), str(table))
    print (sql_command)

    # load the data 
    data = pd.read_sql(sql_command, conn)

    print(data.shape)
    return(data)