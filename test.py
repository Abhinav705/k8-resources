import oracledb
import os
import sys 
import sqlalchemy
import pandas as pd
import time
oracledb.version="8.3.0"
sys.modules["cx_Oracle"]=oracledb

def get_oracle_connection_params():

    try:
        params = {}
        params['ORACLE_DB_SERVER'] = "xxx"
        params['ORACLE_DB_PORT'] = xxx
        params['ORACLE_SERVICE_NAME'] = "xxx"
        params['ORACLE_DB_USER'] = "xxx"
        params['ORACLE_DB_PWD'] = "xxx"
        return params 
    except Exception as error:
        print(error)
        raise 

def fetch_date(sql_query:str)
    try:
        params = get_oracle_connection_params()
        df = pd.DataFrame()
        dsn_string = f"{params['ORACLE_DB_SERVER']}:{params['ORACLE_DB_PORT']}/?service_name={params['ORACLE_SERVICE_NAME']}"
        connection_string = f"oracle://{params["ORACLE_DB_USER"]}:{params['ORACLE_DB_PWD']}@{dsn_string}"
        time.sleep(5)
        conn_engine = sql_alchemy.create_engine(connection_string,pool_pre_ping=True)

        with conn_engine.connect() as conn:
            conn = conn.execution_options(stream_results=True)
            df = pd.read_sql(sql_query,con=conn)
        conn_engine.dispose(close=True)
        return df 
    except Exception as expn:
        print(f"Unable to Fetch data from oracle db:{expn} \n ")
        raise 

def execute_sql(sql_query:str):

    try:
        return_flag = False
        params = get_oracle_connection_params()
        with oracle.connect(user=params['ORACLE_DB_USER'],
                            password=params['ORACLE_DB_PWD'],
                            dsn =f"{params['ORACLE_DB_SERVER']}:{params['ORACLE_DB_PORT']}/{params['ORACLE_SERVICE_NAME']}") as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                connection.commit()
                return_flag=True
        return return_flag
    except Exception as expn:
        print("Unable to execute sql on oracle db: {expn}")
        raise

acctnamefile = "C:/Users/Downlods/text.psv"
sql_query = "select * from all_tables"
df1=pd.DataFrame()
df1=fetch_data(sql_query)
df1.to_csv(acctnamefile,sep="|")
