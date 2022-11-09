# Databricks notebook source
# DBTITLE 1,Importação das funções de apoio
from pyspark.sql.functions import col, base64, lit, concat

# COMMAND ----------

# DBTITLE 1,Path onde as imagens estão armazenadas
path = "/FileStore/imgs/"

# COMMAND ----------

# DBTITLE 1,Leitura do DataFrame
#Leitura em formato binário selecionando apenas arquivos JPG
df = spark.read.format("binaryFile").option("pathGlobFilter", "*.jpg").load(path)

#Criação de coluna base64 
df = df.withColumn("base64", concat( lit("data:image/jpg;base64,"), base64(col("content"))))

#Exibição do dataframe
df.display()
