# ROUND, CAST, MAX, MIN, WHERE, COLLECT
# Import your libraries
import pyspark
from pyspark.sql.functions import col, max, min, round

# Start writing code
cities_density = cities_population.select(
    "country",
    "city",
    round(col("population") / col("area")).cast("int").alias("density")
)
    
max_density = cities_density.select(max(col("density"))) \
                            .collect()[0][0]
                            
min_density = cities_density.select(min(col("density"))) \
                            .collect()[0][0]

extreme_density_cities = cities_density.where(
        (col("density") == min_density) 
        | (col("density") == max_density)
    )

# To validate your solution, convert your final pySpark df to a pandas df
extreme_density_cities.toPandas()