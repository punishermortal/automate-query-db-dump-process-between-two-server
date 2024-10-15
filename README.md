# automate-query-db-dump-process-between-two-server


# Problem Statement

In many organizations, managing databases efficiently is crucial for maintaining data integrity and ensuring that operations run smoothly. However, manual processes for exporting, importing, and modifying data in databases can be time-consuming, error-prone, and difficult to manage. This can lead to inconsistencies, loss of data, and increased operational overhead.


# Database Automation Script

This script automates the process of exporting tables from a client database, exporting an entire triazine database, running specified SQL queries, and importing tables into the triazine database. It utilizes the `mysql.connector` library to connect to MySQL databases and the `subprocess` module to execute MySQL commands.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Logging](#logging)
- [License](#license)

## Prerequisites

Before running the script, ensure you have the following:
- Python 3.x installed on your machine.
- `mysql-connector-python` package installed. You can install it using pip:

  ```bash
  pip install mysql-connector-python

git clone <https://github.com/punishermortal/automate-query-db-dump-process-between-two-server.git>
cd <automate-query-db-dump-process-between-two-server>

pip install -r requirements.txt


# change configuration

client_db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_client_database',
}

triazine_db_config = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'your_triazine_database',
}


# tables_to_export = ['table1', 'table2', 'table3']  # Add your tables here


# SQL queries you want to run in the triazine database

sql_queries = [
    "DROP TABLE IF EXISTS example_table_old;",
    "CREATE TABLE example_table_backup LIKE example_table;",
    # Add more queries as needed
]


python main.py
