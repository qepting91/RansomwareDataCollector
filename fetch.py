import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Setup the database connection
conn = psycopg2.connect(os.environ["DATABASE_URL"])
cur = conn.cursor()

# Query the table
query = """
    SELECT "group", title, COUNT(*) 
    FROM ransomware 
    GROUP BY "group", title 
    HAVING COUNT(*) > 1
"""
cur.execute(query)

# Fetch and print each row
for row in cur.fetchall():
    print(row)

# Close the cursor and the connection
cur.close()
conn.close()
