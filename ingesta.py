import pymysql
import pandas as pd

# Leer archivo CSV
df = pd.read_csv("data.csv")

# Conectar a MySQL
conn = pymysql.connect(
    host='host.docker.internal',
    port=3307,
    user='utec',
    password='1234',
    database='empresa'
)

cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS empleados (
        id INT PRIMARY KEY AUTO_INCREMENT,
        nombre VARCHAR(100),
        correo VARCHAR(100)
    );
""")

# Insertar filas del CSV
for index, row in df.iterrows():
    cursor.execute("INSERT INTO empleados (nombre, correo) VALUES (%s, %s)", (row['nombre'], row['correo']))

conn.commit()
cursor.close()
conn.close()

print("✅ Datos del CSV insertados en la tabla empleados.")