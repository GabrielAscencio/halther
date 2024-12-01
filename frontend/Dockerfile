# Usar la imagen base oficial de Node.js para la construcción
FROM node:16-slim AS build

# Establecer el directorio de trabajo en /app dentro del contenedor
WORKDIR /app

# Copiar el package.json y package-lock.json (si lo tienes)
COPY frontend/package*.json ./

# Instalar las dependencias
RUN npm install

# Copiar todo el código del frontend al contenedor
COPY frontend/ .

# Compilar la aplicación para producción
RUN npm run build

# Usar nginx para servir los archivos estáticos
FROM nginx:alpine

# Copiar los archivos de construcción de la imagen anterior al directorio de nginx
COPY --from=build /app/dist /usr/share/nginx/html

# Exponer el puerto 80 para servir la aplicación
EXPOSE 80

# Iniciar nginx
CMD ["nginx", "-g", "daemon off;"]
