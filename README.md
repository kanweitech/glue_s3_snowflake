![alt text](https://github.com/kanweitech/glue_s3_snowflake/blob/main/images/glue.png)

### Objective
The goal of this project is to automate the extraction, loading and transformation (ELT) of sales data from multiple countries into snowflake, utilizing AWS Glue, S3 and Snowpark for a seamless processing.

### Data Sources
The sales order files are stored in a Github repository, with different formats for each country

- **india**: CSV format
- **USA**: Parquet format
- **France**: JSON format

### ELT Process
**1. Data Extraction and Storage(AWS Glue & S3)**
- AWS Glue will be used to execute a Python script that connects to the GitHub repository.
- The script will extract the sales data for India, USA and France.

![alt text](https://github.com/kanweitech/glue_s3_snowflake/blob/main/images/glue_s3_snowpark_1.png)

![alt text](https://github.com/kanweitech/glue_s3_snowflake/blob/main/images/glue_s3_snowpark_2.png)
   

- The Extracted files will be loaded into an AWS S3 bucket

![alt text](https://github.com/kanweitech/glue_s3_snowflake/blob/main/images/s3_bucket_with_data.png)

**2. Data Loading into Snowflake (Snowpark and Staging Schema)**
- Using Snowpark, the data will ingested from S3 into snowflake.
- the files will be loaded into their respective tables under the **STAGING** schema and using the **COPY** command.
- After initial validation, the data will be moved from **STAGING** schema into **RAW** schema.



