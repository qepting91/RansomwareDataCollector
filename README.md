# RansomwareDataCollector
RansomwareDataCollector is a Python application designed to scrape and store data on ransomware attacks. The application extracts data from a specified source, stores the information in a CockroachDB database. See https://github.com/qepting91/streamlitransomware for the visualization step of this collection.

## Features
Scrapes ransomware attack data from a specified source.
Stores the collected data in a CockroachDB database.

## Getting Started
These instructions will guide you on how to run this project on your local machine for development and testing purposes.

## Prerequisites
Python 3.x
PostgreSQL/CockroachDB
Python dependencies as listed in requirements.txt
Installation
Clone the repository to your local machine.
'''
bash
git clone https://github.com/yourusername/RansomwareDataCollector.git
'''
Navigate to the project directory.
'''
bash
cd RansomwareDataCollector
'''
Install the necessary Python dependencies.
'''
bash
pip install -r requirements.txt
'''

## Set up the database.

Ensure PostgreSQL or CockroachDB is installed and running.
Create a new database and table for storing the data.
Set the DATABASE_URL environment variable to the connection string for your database.
Run the scraper.py script to collect ransomware attack data.
'''
bash
python scraper.py
'''

## Usage
This scraper collects the data and stores it in the CockroachDB. You can use the fetch.py file to query the database as you wish. 
The data scraping process can be automated using a task scheduler like cron (Linux/macOS) or Task Scheduler (Windows).
You can create an executable version of the Python script using libraries like PyInstaller or cx_Freeze.
## Contributing
Contributions are welcome! Please read the contributing guidelines first.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
CockroachDB: for the resilient SQL database for global business.
PyInstaller: for the simple packaging of Python applications into stand-alone executables.
