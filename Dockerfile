# Imagen base ligera con Python
FROM python:3.10-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar script y CSV al contenedor
COPY ingesta.py .
COPY data.csv .

# Instalar dependencias directamente
RUN pip install --no-cache-dir pymysql pandas boto3

# Comando por defecto
CMD ["python", "ingesta.py"]
