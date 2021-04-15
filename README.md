# USA-Immigration Data Warehouse 

### Project Motivation
Many people travel to USA for different purposes, the TSA (Transport Security Administration)
is interested to know in depth the immigration patterns in a monthly basis by the airport based on different
factors, such as immigration data, temperature, US Demographics and Airport Codes.

This project provides a data warehouse, which will allow different TSA members to access 
curated data that can be use for making reports and deeper analytics insights 
related to migration traveler patterns.

The project involves different cloud technologies, such as Redshift, pySpark and Apache AirFlow

## Datasets 

- I94 Immigration Data: This data comes from the US National Tourism and Trade Office. ([Source](https://travel.trade.gov/research/reports/i94/historical/2016.html))
- World Temperature Data: This dataset came from Kaggle. ([Source](https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data))
- U.S. City Demographic Data: This data comes from OpenSoft. ([Source](https://public.opendatasoft.com/explore/dataset/us-cities-demographics/export/))
- Airport Code Table: This is a simple table of airport codes and corresponding cities. ([Source](https://datahub.io/core/airport-codes#data))

## Project Structure
    .
    │
    ├── dags     
    │   ├── immigration_etl_dag.py                # Contains the main ETL dag
    │   ├── dwh.cfg                               # Credentials config file
    │   └── datasets 
    │       ├── README.md                         # Specify which datasets whould be downloaded
    │       ├── sas_data                          # Folder with SAS files please reffer to README.md
    │       ├── airport-codes_csv.csv             # airport codes please reffer to README.md
    │       ├── GlobalLandTemperatureByCity.csv   # temperature dataset please reffer to README.md
    │       ├── I94_SAS_Labels_Description.SAS    # I94 SAS labels please reffer to README.md
    │       ├── immigration_data_sample.csv       # Immigration data please reffer to README.md
    │       └── us-cities-demographics.csv        # US demographics please reffer to README.md
    │   
    ├── plugins                   
    │   ├── helpers
    │   │   ├── __init__.py
    │   │   └── table_configs.py                  # Table tests and S3 storage buckets
    │   │
    │   ├── operators        
    │   │   ├── __init__.py
    │   │   ├── copy_redshift.py                  # Custom Operator to load data from S3 into Redshift
    │   │   ├── data_quality.py                   # Custom Operator to perform some data quality checks
    │   │   └── sas_value_redshift.py             # Custom Operator for extracting data from SAS source code      
    │   └── __init__.py
    │    
    ├── tables                   
    │   ├── create_tables.py                      # create tables script
    │   ├── sql_queries.py                        # RAW queries to create the project tables
    │   └── dwh.cfg                               # Credentials config file
    │
    ├── Capstone_Proyect.ipynb                    # Project analysis, developmet and design (Jupyter Noteboook)
    ├── Capstone_Proyect.html                     # Project analysis, development and design (HTML)
    ├── docker-compose.yaml                       # Apache AirFlow docker yaml file
    ├── LICENSE 
    ├── notebook_images                           # Diagrams and support images
    └── README.md                                 
    
    
## Project implementation details
The details around the data exploration, datasets, ETL (Extract-Transform-Load) design, data model, assumptions are located 
in the file **Capstone_Project.ipynb**

## How to run the ETL

1. Clone the repository and fill the credential information in tables/dwh.cfg and dags/dw.cfg
2. Read the file dags/datasets/README.md (It will tell you about the datasets needed)
3. Upload those datasets in a S3 bucket
4. Please follow the instructions to run Apache Airflow in a Docker container [Instructions](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html))
5. **Apache AirFlow 2.0.1 has an error in the official documentation, and I created a video to fix it and 
share it with the world (Sharing is caring) [FIX THAT BUG](https://youtu.be/RVKRtgDIh8A))**
6. Go to the main folder project and is Apache AirFlow is not running do:

```
docker compose up  (Start the services)
docker compose down (Stop the services)
```
7. Configure the connector in Apache Airflow to be able to see Amazon Redshift [Detailed Steps](https://www.progress.com/tutorials/jdbc/connect-to-redshift-salesforce-and-others-from-apache-airflow)
8. You should be able to see the DAG -> immigration_etl_dag in ApacheAirflow
9. **Run the script tables/create_tables.py**
10. Finally, in Apache AirFlow you can execute the dag and wait for the results.

## Requirements

- AWS Redshift Configured or AWS RDS Postgres Database or a local database (Some SQL queries may need to be adapted to support this case) 
- Docker -> Apache AirFlow (2.0.1) with the connector configuration
- Python 3

