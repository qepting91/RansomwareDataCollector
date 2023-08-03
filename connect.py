import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

# Setup the database connection
conn = psycopg2.connect(os.environ["DATABASE_URL"])
cur = conn.cursor()

# Create the table
table_creation_query = """
CREATE TABLE IF NOT EXISTS ransomware(
    id SERIAL PRIMARY KEY,
    "group" VARCHAR(255) NOT NULL,
    title VARCHAR(255) NOT NULL,
    date DATE NOT NULL
);
"""
cur.execute(table_creation_query)

# Commit changes and close the connection
conn.commit()
cur.close()
conn.close()