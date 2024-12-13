# Usar la imagen base oficial de Node.js para la construcción
FROM node:16-slim AS build

# Establecer el directorio de trabajo en /app dentro del contenedor
WORKDIR /halther/frontend

# Copiar el package.json y package-lock.json (si lo tienes)
COPY ./frontend/package*.json .

# Instalar las dependencias
RUN npm install

# Copiar todo el código del frontend al contenedor
COPY ./frontend/ .

# Compilar la aplicación para producción
RUN npm run build
RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "80"]

# Usar nginx para servir los archivos estáticos
FROM nginx:alpine
# Copiar los archivos de construcción de la imagen anterior al directorio de nginx
COPY --from=build /halther/frontend/dist /usr/share/nginx/html

# Copiar el archivo nginx.conf al contenedor
COPY ./frontend/nginx.conf /etc/nginx/nginx.conf
# Copiar el archivo nginx.conf al contenedor
COPY ./frontend/default.conf /etc/nginx/conf.d/default.conf

# Exponer el puerto 80 para servir la aplicación
EXPOSE 80

# Iniciar nginx
CMD ["nginx", "-g", "daemon off;"]

RUN echo $NODE_ENV
