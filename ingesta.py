import pandas as pd
import pymysql
import boto3
# Leer archivo CSV
df = pd.read_csv("data.csv")

# Conectar a MySQL
conn = pymysql.connect(
    host='mysql_datos',
    port=3306,
    user='root',
    password='utec',
    database='empresa'
)

# Leer los datos
df = pd.read_sql("SELECT * FROM empleados", conn)
conn.close()

# Guardar como CSV
csv_file = "data.csv"
df.to_csv(csv_file, index=False)

# Subir a S3
s3 = boto3.client('s3')
s3.upload_file(csv_file, "yit-output-02", csv_file)

print("Ingesta completada desde MySQL")
