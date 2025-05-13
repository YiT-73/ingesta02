import pymysql
import pandas as pd

# Leer archivo CSV
df = pd.read_csv("data.csv")

# Conectar a MySQL
conn = pymysql.connect(
    host='54.227.17.26 ',
    port=3307,
    user='utec',
    password='1234',
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
s3.upload_file(csv_file, "gcr-output-01", csv_file)

print("Ingesta completada desde MySQL")
