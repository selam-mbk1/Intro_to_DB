import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to the MySQL Server
        connection = mysql.connector.connect(
            host='localhost',
            user='root',           # Replace with your MySQL username
            password='your_pass'   # Replace with your MySQL password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database without using SELECT or SHOW
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as err:
        print(f"Error: {err}")

    finally:
        # Cleanup: Close cursor and connection
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    create_database()
