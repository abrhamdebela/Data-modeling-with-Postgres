Project: NoSQL Data modeling with Cassandra

Introduction 

A startup Called Sparkify , they need to analyze data which they collecting from songs and user the app. the source data is in CSV format and its partitioned in time. Which need to be transfer and load in to Cassandra database for detail analysis. 

Project overview

To accomplish the project, I used PYTHON and CQL script to remove the partition and to append the entire data in to one file.  And using those data and apply  ETL process  in Casandra environment and run the select query to test if the tables are created properly and to test the data are populated/insert in to the table accordingly. 
Data source: 
The data source used one CSV data source called even_data and it partitioned by time and it transfer into one single data called event_data_new.csv, which we are using it for our analysis and ETL.
 
Steps to complete the Project:

1)	 Combing the partition data in to one CSV file by using python language 
2)	 CREATE KEYSPACE and then SET KEYSPACE statements 
3)	 Created Tables according to select query, which we need to return. 
4)	 On this step, we will apply the ETL process; first extract data from CSV and insert /load it in to the table and by using python library will transfer CSV format into Cassandra format and it will iterate in each row and insert it in the table. 
5)	 Finally drop the tables and close the connection 
  Note: - table creation in Cassandra is depending on the criteria of the query request. Whenever we need some different query, we have to create new table for that specific query.

