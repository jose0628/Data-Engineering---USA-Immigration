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
    │   ├── immigration_etl_gad.py                # Contains the main ETL dag
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
    │   │   ├── copy_redshift.py                  # Operator to load data from S3 into Redshift
    │   │   ├── data_quality.py                   # Operator to perform some data quality checks
    │   │   └── sas_value_redshift.py             #       
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
    └── README.md                                 
    
    


## Project implementation details
The details around the data exploration, datasets, ETL (Extract-Transform-Load) design, data model, assumptions are located 
in the file **Capstone_Project.ipynb**

## How to run

1. Please follow the instructions to run Apache Airflow in a Docker container [Instructions](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html))
2. **Apache AirFlow 2.0.1 has an error in the official documentation, and I created a video to fix it and 
share it with the world (Sharing is caring) [FIX THAT BUG](https://youtu.be/RVKRtgDIh8A))**
3. Clone the repository and all the datasets should be in the **dags** folder (It will be loaded in the docker volume based on the official Apache AirFlow 2.0.1 yaml file)

4. Configure your connector to your Redshift, RDS or local database instance
4. Find the dag for this project and run it.

##### Side notes: Apache AirFlow 2.0.1 yaml file (it is also in step 2)
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'
```

## Requirements

- AWS Redshift Configured or AWS RDS Postgres Database or a local database (Some SQL queries may need to be adapted to support this case) 
- Docker -> Apache AirFlow (2.0.1) with the connector configuration
- Python 3

