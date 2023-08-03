import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def delete_data():
    # Set up the database connection
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()

    # Delete all rows from the ransomware table
    cur.execute("DELETE FROM ransomware")

    # Commit changes and close the database connection
    conn.commit()
    cur.close()
    conn.close()

delete_data()
