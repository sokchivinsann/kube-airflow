import os
from pyspark.sql import SparkSession
import re
from datetime import datetime, timedelta

def build_spark(app_name: str) -> SparkSession:
    return (
        SparkSession.builder
        .appName(app_name)
        .config("spark.ui.enabled", "false")
        .config("spark.sql.parquet.mergeSchema", "false")
        # S3A / PowerScale settings — one place, all jobs
        # .config("spark.hadoop.fs.s3a.endpoint", os.getenv("S3_ENDPOINT"))
        # .config("spark.hadoop.fs.s3a.access.key", os.getenv("S3_ACCESS_KEY"))
        # .config("spark.hadoop.fs.s3a.secret.key", os.getenv("S3_SECRET_ACCESS_KEY"))
        .config("spark.hadoop.fs.s3a.path.style.access", "true")
        .config("spark.hadoop.fs.s3a.connection.ssl.enabled", "false")
        .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        .config("spark.hadoop.fs.s3a.directory.marker.retention", "keep")
        .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version",2)
        .getOrCreate()
    )

if __name__ == "__main__":
	spark = build_spark("my_spark_app")
	# read data from local file system
	df = spark.read.csv("data/input.csv", header=True, inferSchema=True)
	df.show()
    
# https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml

# http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/login