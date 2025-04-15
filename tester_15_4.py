import os
import snowflake.connector

def get_snowflake_connection():
    try:
        conn = snowflake.connector.connect(
            user="SNOWMIG25",
            password="Manivannanmurugan2",
            account="QMMWEOV-SA29993",
            warehouse="COMPUTE_WH",
            database="MANI",
            schema="MANI",
            role="ACCOUNTADMIN"
        )
        print("Connected to Snowflake.")
        return conn
    except Exception as e:
        print(f"Error connecting to Snowflake: {e}")
        exit(1)

def read_sql_file(file_path):
    try:
        with open(file_path, 'r') as file:
            sql_script = file.read()
        return sql_script
    except Exception as e:
        print(f"Error reading SQL file: {e}")
        exit(1)

def execute_sql_script(conn, sql_script):
    try:
        cursor = conn.cursor()
        for statement in sql_script.split(';'):
            if statement.strip():
                print(f"Executing:\n{statement.strip()[:100]}...")
                cursor.execute(statement)
        cursor.close()
        print("Migration completed successfully.")
    except Exception as e:
        print(f"Error executing SQL: {e}")
        exit(1)

if __name__ == "__main__":
    conn = get_snowflake_connection()
    sql = read_sql_file("C:/Users/manivannan.m/Downloads/test.sql")
    execute_sql_script(conn, sql)
    conn.close()

