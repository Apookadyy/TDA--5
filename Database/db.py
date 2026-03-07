import sqlite3

DB_NAME = "app_database.db"


def get_connection():
    """
    Create database connection
    """
    conn = sqlite3.connect(DB_NAME)
    return conn


def create_table():
    """
    Create table if not exists
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        value INTEGER
    )
    """)

    conn.commit()
    conn.close()


def insert_data(value):
    """
    Insert data into table
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO data (value) VALUES (?)", (value,))
    conn.commit()

    conn.close()


def fetch_data():
    """
    Fetch all data from table
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data")
    rows = cursor.fetchall()

    conn.close()

    return rows