import sys
from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max
from pyspark.sql.window import Window


# command to execute
# spark-submit Recreating.py 2019 01

def main(argv):
    input_basepath = "s3://bnc-datamigration-temp-bucket-dev-20181106/Temp-dataset"
    output_basepath = "s3://bnc-datamigration-temp-bucket-dev-20181106/Results"
    yyyy = argv[0]
    mm = argv[1]
    env = argv[1]
    if 'PROD' == env:
        input_basepath = "s3://market-data-ticker/block-explorer-parquet"
        output_basepath = "s3://market-data-migration/block-explorer-last-reported"

    conf = SparkConf()
    spark = SparkSession \
        .builder \
        .appName("FetchLastReportedSupply") \
        .getOrCreate()
    df = spark.read.csv('/'.join([input_basepath, yyyy, mm, '*/*']))
    result = df.withColumn("ts", col("date").cast('timestamp')).drop("date")
    result.persist()
    w = Window.partitionBy("symbol").orderBy("ts").rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)
    last_df = result.select('symbol', 'open', 'close', 'low', 'high', 'volume', 'ts',
                           max(col('ts')).over(w).alias('last_reported_ts')).where(
        (col('ts') == col('last_reported_ts')))
    last_df.repartition(1).write.csv('/'.join([output_basepath, yyyy, mm]), header='true')


if __name__ == "__main__":
    main(sys.argv[1:])
