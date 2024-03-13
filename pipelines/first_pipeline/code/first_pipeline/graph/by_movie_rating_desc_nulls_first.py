from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from first_pipeline.config.ConfigStore import *
from first_pipeline.udfs.UDFs import *

def by_movie_rating_desc_nulls_first(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.orderBy(col("movie_averageRating").asc())
