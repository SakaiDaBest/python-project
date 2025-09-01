import psycopg2

def get_last_rowid():
    conn = psycopg2.connect(
        host="your_postgres_host",
        database="your_postgres_db",
        user="your_postgres_user",
        password="your_postgres_password"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(rowid) FROM sales_data;")
    last_rowid = cursor.fetchone()[0]
    conn.close()
    return last_rowid if last_rowid else 0
import mysql.connector

def get_latest_records(last_rowid):
    conn = mysql.connector.connect(
        host="your_mysql_host",
        database="your_mysql_db",
        user="your_mysql_user",
        password="your_mysql_password"
    )
    cursor = conn.cursor()
    query = "SELECT * FROM sales_data WHERE rowid > %s;"
    cursor.execute(query, (last_rowid,))
    records = cursor.fetchall()
    conn.close()
    return records

def insert_records(records):
    conn = psycopg2.connect(
        host="your_postgres_host",
        database="your_postgres_db",
        user="your_postgres_user",
        password="your_postgres_password"
    )
    cursor = conn.cursor()
    insert_query = "INSERT INTO sales_data (rowid, date, region, product, quantity, price) VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.executemany(insert_query, records)
    conn.commit()
    conn.close()
