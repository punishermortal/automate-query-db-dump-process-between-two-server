import subprocess
import mysql.connector
import logging
import os
import time

logging.basicConfig(
    filename='database_automation.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class DatabaseAutomation:
    def __init__(self, client_db_config, triazine_db_config):
        self.client_db_config = client_db_config
        self.triazine_db_config = triazine_db_config
        logging.info("DatabaseAutomation initialized.")

    def export_tables_from_client_db(self, tables):
        for table in tables:
            logging.info(f"Exporting table '{table}' from the client database.")
            result = subprocess.run(
                f"mysqldump -u {self.client_db_config['user']} -p{self.client_db_config['password']} "
                f"{self.client_db_config['database']} {table} > {table}.sql", 
                shell=True
            )
            if result.returncode == 0:
                logging.info(f"Successfully exported '{table}'.")
            else:
                logging.error(f"Failed to export '{table}'.")
                return False
        return True

    def export_triazine_db(self):
        logging.info("Exporting the entire triazine database.")
        result = subprocess.run(
            f"mysqldump -u {self.triazine_db_config['user']} -p{self.triazine_db_config['password']} "
            f"{self.triazine_db_config['database']} > triazine_database.sql", 
            shell=True
        )
        if result.returncode == 0:
            logging.info("Successfully exported the triazine database.")
            return True
        else:
            logging.error("Failed to export the triazine database.")
            return False

    def run_sql_queries(self, queries):
        logging.info("Running SQL queries in the triazine database.")
        try:
            connection = mysql.connector.connect(**self.triazine_db_config)
            cursor = connection.cursor()
            
            for query in queries:
                logging.info(f"Executing query: {query}")
                cursor.execute(query)
            
            connection.commit()
            logging.info("SQL queries executed successfully.")
            return True
        except mysql.connector.Error as err:
            logging.error(f"Error occurred: {err}")
            return False
        finally:
            cursor.close()
            connection.close()

    def import_tables_to_triazine_db(self, tables):
        for table in tables:
            logging.info(f"Importing table '{table}' into the triazine database.")
            result = subprocess.run(
                f"mysql -u {self.triazine_db_config['user']} -p{self.triazine_db_config['password']} "
                f"{self.triazine_db_config['database']} < {table}.sql", 
                shell=True
            )
            if result.returncode == 0:
                logging.info(f"Successfully imported '{table}'.")
            else:
                logging.error(f"Failed to import '{table}'.")
                return False
        return True

    def automate(self, tables, queries):
        logging.info("Starting automation process.")

        success = True
        
        if not self.export_tables_from_client_db(tables):
            success = False
            
        if not self.export_triazine_db():
            success = False
            
        if not self.run_sql_queries(queries):
            success = False
            
        if not self.import_tables_to_triazine_db(tables):
            success = False
            
        if success:
            logging.info("Automation completed successfully.")
        else:
            logging.error("Automation completed with errors.")

if __name__ == "__main__":

    client_db_config = {
        'host': 'localhost',
        'user': 'bhaiji',
        'password': 'mortal@1',
        'database': 'abc',
    }

    triazine_db_config = {
        'host': 'localhost',
        'user': 'bhaiji',
        'password': 'mortal@1',
        'database': 'cogta',
    }

    tables_to_export = ['accounts', 'afiliados','obligations','offers','payins','payouts','total_data','transacciones','users','zoho_accounts','zoho_customerpayments','zoho_invoices','zoho_proyectos','repayments']
    
    sql_queries = [
        "DROP TABLE IF EXISTS accounts_old;"
        "DROP TABLE IF EXISTS afiliados_old;"
        "DROP TABLE IF EXISTS obligations_old;"
        "DROP TABLE IF EXISTS offers_old;"
        "DROP TABLE IF EXISTS payins_old;"
        "DROP TABLE IF EXISTS payouts_old;"
        "DROP TABLE IF EXISTS total_data_old;"
        "DROP TABLE IF EXISTS transacciones_old;"
        "DROP TABLE IF EXISTS users_old;"
        "DROP TABLE IF EXISTS zoho_accounts_old;"
        "DROP TABLE IF EXISTS zoho_customerpayments_old;"
        "DROP TABLE IF EXISTS zoho_invoices_old;"
        "DROP TABLE IF EXISTS zoho_proyectos_old;"
        "DROP TABLE IF EXISTS repayments_old;"
        "CREATE TABLE accounts_backup LIKE accounts;"
        "RENAME TABLE accounts TO accounts_old;"
        "RENAME TABLE accounts_backup TO accounts;"
        "CREATE TABLE afiliados_backup LIKE afiliados;"
        "RENAME TABLE afiliados TO afiliados_old;"
        "RENAME TABLE afiliados_backup TO afiliados;"
        "CREATE TABLE obligations_backup LIKE obligations;"
        "RENAME TABLE obligations TO obligations_old;"
        "RENAME TABLE obligations_backup TO obligations;"
        "CREATE TABLE offers_backup LIKE offers;"
        "RENAME TABLE offers TO offers_old;"
        "RENAME TABLE offers_backup TO offers;"
        "CREATE TABLE payins_backup LIKE payins;"
        "RENAME TABLE payins TO payins_old;"
        "RENAME TABLE payins_backup TO payins;"
        "CREATE TABLE payouts_backup LIKE payouts;"
        "RENAME TABLE payouts TO payouts_old;"
        "RENAME TABLE payouts_backup TO payouts;"
        "CREATE TABLE total_data_backup LIKE total_data;"
        "RENAME TABLE total_data TO total_data_old;"
        "RENAME TABLE total_data_backup TO total_data;"
        "CREATE TABLE transacciones_backup LIKE transacciones;"
        "RENAME TABLE transacciones TO transacciones_old;"
        "RENAME TABLE transacciones_backup TO transacciones;"
        "CREATE TABLE users_backup LIKE users;"
        "RENAME TABLE users TO users_old;"
        "RENAME TABLE users_backup TO users;"
        "CREATE TABLE zoho_accounts_backup LIKE zoho_accounts;"
        "RENAME TABLE zoho_accounts TO zoho_accounts_old;"
        "RENAME TABLE zoho_accounts_backup TO zoho_accounts;"
        "CREATE TABLE zoho_customerpayments_backup LIKE zoho_customerpayments;"
        "RENAME TABLE zoho_customerpayments TO zoho_customerpayments_old;"
        "RENAME TABLE zoho_customerpayments_backup TO zoho_customerpayments;"
        "CREATE TABLE zoho_invoices_backup LIKE zoho_invoices;"
        "RENAME TABLE zoho_invoices TO zoho_invoices_old;"
        "RENAME TABLE zoho_invoices_backup TO zoho_invoices;"
        "CREATE TABLE zoho_proyectos_backup LIKE zoho_proyectos;"
        "RENAME TABLE zoho_proyectos TO zoho_proyectos_old;"
        "RENAME TABLE zoho_proyectos_backup TO zoho_proyectos;"
        "CREATE TABLE repayments_backup LIKE repayments;"
        "RENAME TABLE repayments TO repayments_old;"
        "RENAME TABLE repayments_backup TO repayments;"
    ]

    # Create an instance of DatabaseAutomation
    db_automation = DatabaseAutomation(client_db_config, triazine_db_config)
    
    # Run the automation
    db_automation.automate(tables_to_export, sql_queries)







