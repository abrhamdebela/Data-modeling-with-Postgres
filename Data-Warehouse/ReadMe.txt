The project focused on design and built data warehouse in the cloud for the analytics purpose for the music streaming app Sparkify.
The ETL and data warehouses built in AWS. 

The design of the database is stare schema, the script written by python. Stare schema have four dimension table and one fact table. Fact table uniquely identify by the “songplays” column which generate from identity and it increment whenever new value add in to the fact table. 

Staging : 

Before it populated the destination table of fact and dimension. Data first insert in to event and song staging table. Staging tables get their data from S3 bucket. 

Dimension table : 

The dimensions table data extracted either from event or song staging tables. To avoid duplication in dimension tables, I applied common table expression and window function in one of the column in each dimension tables. 

Fact table :

Fact table’s data populated from both song and event staging table. The column name “songplay_id” uniquely identify the fact table. songplay_id generate from identity and it increment whenever new value add in the fact table. 

                            The project contain the below listed component 
                            
  IAC: - it will help us to create cloud infrastructure, to check the list of column name in S3, which will help us when we create tables.
  sql_queries:- to create tables, to insert data from staging tables and insert data in to staging from s3 
  etl: - it run the sq_querirs.py, which can extract data from source to destination 
  create_tables : - it trigger the sql_queries to create table for staging , dimension and fact tables .
  column_analysis :- to analysis the columns content in our raw JSON source data for our tables. 
  

Finally, 

Fact, dimension, and staging tables will be create on redshift when we run the python code on the following step in the terminal:
1st)  run IAC to get host, permission to access Redshift from S3 and to check the list of column in the file, which it can help us when we create tables.
2nd)  run: - python create_tables.py 
3nd) run:-python etl.py 
  
  
  
  
  
