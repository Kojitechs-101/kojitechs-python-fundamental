# password, dbname, username, port, host/endpoint
import psycopg2
from pprint import pprint
import time
import os
import json 
from pathlib import Path


DB_USER = os.environ['DB_NAME']
DB_HOST = os.environ['DB_HOST']
DB_NAME = os.environ['DB_NAME']
DB_PASSWORD = os.environ['DB_PASSWORD']

"""
try:
    with psycopg2.connect(user=DB_USER, database=DB_NAME, password=DB_PASSWORD, host=DB_HOST) as conn:
        cursor = conn.cursor()
        print(conn.get_dsn_parameters(), "\n")
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print(f"You are connected to postgres version {record}")

except Exception as err:
    print(err)
"""

## CREATE A DATABASE TABLES USING PYTHON

try:
    with psycopg2.connect(user=DB_USER, database=DB_NAME, password=DB_PASSWORD, host=DB_HOST) as conn:
        cursor = conn.cursor()
        print("creating table in database...")
        time.sleep(4)
        create_table = """CREATE TABLE kojitechs
                        (ID INT PRIMARY KEY NOT NULL, FIRST_NAME  TEXT NOT NULL ,
                        LAST_NAME   TEXT NOT NULL,
                        PRICE   REAL);"""
        cursor.execute(create_table)
        conn.commit()
        print("Table created successfuly....")

except Exception as err:
    print(err)