import configparser
import psycopg2
from sql_queries import copy_table_queries, insert_table_queries


def load_staging_tables(cur, conn):
    """
   The function iterates each tables to copy from S3 bucket and populate into staging tables with out any transformation 
   
    """
    for query in copy_table_queries:
        cur.execute(query)
        conn.commit()


def insert_tables(cur, conn):
    """
    This function iterate each table and execute it to insert the values into dimension and fact table from staging tables 
    """
    for query in insert_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    This main function read the config file, establish connection, and call the above-mentioned function.
    """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()
    
    load_staging_tables(cur, conn)
    insert_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()