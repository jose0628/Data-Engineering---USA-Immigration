# USA-Immigration Data Warehouse 

### Project Motivation
Many people travel to USA for different purposes, the TSA (Transport Security Administration)
is interested to know in depth the immigration patterns in a monthly basis based on different
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
    ├── dl_template.cfg  # ERM cluster credentials, it should be rename it as dl.cfg
    └── etl.py           # Reads data from S3, processes that data using Spark, and writes them back to S3

## Project implementation details
The details around the data exploration, ETL (Extract-Transform-Load) design, data model, assumptions are located 
in the file **Capstone_Project.ipynb**

## How to run

1. Please follow the instructions to run Apache Airflow in a Docker container [Instructions](https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html))
2. **Apache AirFlow 2.0.1 has an error in the official documentation, and I created a video to fix it and 
share it with the world (Sharing is caring) [FIX THAT BUG](https://youtu.be/RVKRtgDIh8A))**
3. Clone the repository and all the datasets should be in the **dags** folder (It will be loaded in the docker volume based on the official Apache AirFlow 2.0.1 yaml file)
4. Find the dag for this project and run it.

##### Side notes: Apache AirFlow 2.0.1 yaml file (it is also in step 2)
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.0.1/docker-compose.yaml'
```

## Requirements

- AWS Redshift Configured
- Docker -> Apache AirFlow (2.0.1) with the connector configuration
- Python 3

