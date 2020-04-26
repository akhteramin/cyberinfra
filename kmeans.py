# u'2.2.0'
from pyspark.sql import SQLContext

sqlContext = SQLContext("sc")
df = sqlContext.createDataFrame([[0, 33.3, -17.5],
                              [1, 40.4, -20.5],
                              [2, 28., -23.9],
                              [3, 29.5, -19.0],
                              [4, 32.8, -18.84]
                             ],
                              ["other","lat", "long"])

df.show()