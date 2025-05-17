import pandas as pd
import pymysql
import boto3
import os

# === Conexión a la base de datos MySQL ===
try:
    conn = pymysql.connect(
        host='mysql_datos',   # nombre del contenedor si usas Docker Compose
        port=3306,
        user='root',
        password='utec',
        database='empresa'
    )
    print("✅ Conexión a MySQL exitosa")
except Exception as e:
    print(f"❌ Error al conectar con MySQL: {e}")
    exit()

# === Leer los datos de la tabla empleados ===
try:
    df = pd.read_sql("SELECT * FROM empleados", conn)
    conn.close()
    print("✅ Datos leídos correctamente de MySQL")
except Exception as e:
    print(f"❌ Error al leer los datos de MySQL: {e}")
    conn.close()
    exit()

# === Guardar los datos en un archivo CSV ===
csv_file = "data.csv"
try:
    df.to_csv(csv_file, index=False)
    print(f"✅ Archivo CSV '{csv_file}' guardado correctamente")
except Exception as e:
    print(f"❌ Error al guardar CSV: {e}")
    exit()

# === Subir el archivo a Amazon S3 ===

# Asegúrate de tener configuradas las siguientes variables de entorno:
# AWS_ACCESS_KEY_ID y AWS_SECRET_ACCESS_KEY
# Puedes exportarlas temporalmente en tu terminal:
# export AWS_ACCESS_KEY_ID="tu_access_key"
# export AWS_SECRET_ACCESS_KEY="tu_secret_key"

try:
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    
    s3.upload_file(csv_file, "yit-output-02", csv_file)
    print("✅ Archivo subido correctamente a S3: yit-output-02")
except Exception as e:
    print(f"❌ Error al subir archivo a S3: {e}")
