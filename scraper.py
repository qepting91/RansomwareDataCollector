import requests
import json
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_data():
    url = "https://raw.githubusercontent.com/joshhighet/ransomwatch/main/posts.json"
    response = requests.get(url)
    data = json.loads(response.text)
    formatted_data = [(d['post_title'], d['group_name'], d['discovered'][:10]) for d in data]
    return formatted_data

def write_to_cockroachdb(data):
    # Set up the database connection
    conn = psycopg2.connect(os.environ["DATABASE_URL"])
    cur = conn.cursor()

    # Query existing rows in the database
    cur.execute("SELECT title, \"group\", date FROM ransomware")
    existing_data = cur.fetchall()

    # Convert existing rows to a set for fast lookup
    existing_rows = set(existing_data)

    # Write data to the database
    for row in data:
        # Skip rows that already exist in the database
        if row in existing_rows:
            continue

        cur.execute("INSERT INTO ransomware (title, \"group\", date) VALUES (%s, %s, %s)", row)

    # Commit changes and close the database connection
    conn.commit()
    cur.close()
    conn.close()

data = fetch_data()
write_to_cockroachdb(data)
