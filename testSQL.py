'''
In this project, we practice SQL using python
'''
import logging
import sqlite3

# Configure logging to write to a file, appending new logs to the existing file
logging.basicConfig(filename='log.txt', level=logging.DEBUG, filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Program started")
logging.info("Program ended")



def execute_sql_from_file(db_filepath, sql_file):
    with sqlite3.connect(db_filepath) as conn:
        with open(sql_file, 'r') as file:
            sql_script = file.read()
        conn.executescript(sql_script)
        print(f"Executed SQL from {sql_file}")

def main():
    db_filepath = 'World.db'
    # Create database schema and populate with data
    '''
    This stament will drop table if it is already exists
    '''
    execute_sql_from_file(db_filepath, 'drop_tables.sql')
    '''
    This stament will create table if it is already exists
    '''
    execute_sql_from_file(db_filepath, 'create_tables.sql')
    '''
    This stament will insert the data into the  table if it is already exists
    '''
    execute_sql_from_file(db_filepath, 'insert_records.sql')
    '''
    select the data from the table 
    '''
    execute_sql_from_file(db_filepath, 'select_records.sql')    
    '''
    update the data to the table .
    '''
    execute_sql_from_file(db_filepath, 'update_records.sql')
    '''
    delete the record from the table 
    '''
    execute_sql_from_file(db_filepath, 'delete_records.sql')
    '''
    daat will display in ascending order 
    '''
    execute_sql_from_file(db_filepath, 'query_sorting.sql')
    '''
    it will display department based employee counts 
    '''
    execute_sql_from_file(db_filepath, 'query_group_by.sql')
    '''
    join employee and department tables 
    '''
    execute_sql_from_file(db_filepath, 'query_join.sql')
    

    logging.info("All SQL operations completed successfully")
    
main()