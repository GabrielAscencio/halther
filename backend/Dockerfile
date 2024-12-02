# Usar la imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /halther/backend dentro del contenedor
WORKDIR /halther/backend

# Copiar el archivo requirements.txt de tu máquina local al contenedor
COPY backend/requirements.txt /halther/backend/

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto del código del backend
COPY . .

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Ejecutar el backend Flask
CMD ["python", "app.py"]
