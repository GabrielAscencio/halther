# Halther local
## Pero si en fa 👉

Aprende a poner y ejecutar halther en tu PC - MacOS todavía no hago tutorial.
Sí cambian algunas cosas entre sistemas operativos. Tambien luego hago del Linux.
Si ya le ultra sabes al linux, primero dejame decirte que:

👉😏👉que pro 😎🐕‍🦺
No tendrás ni problemas para hacer todo esto e incluso buildear sin tutoriales.

## Windows 🪟

**Obligatorio** - Instala Git para windows.
**Obligatorio** - Instala Docker Desktop
Requerido para buildear - Instala Node.js para windows
Requerido para buildear - Instala Python 13.12 para windows o superior.
Opcional - Instala Visual Studio Code

Si ya los tienes procura actualizarlos.

### Una vez instalado todo eso.

- Abre una terminal y navega a la raiz de tu unidad principal.
  
  `cd C:`

- usa git clone
  
  `git clone https://github.com/GabrielAscencio/halther.git`

#### Vas a construir los paquetes en tu entorno

- en tu terminal ejecuta navega al directorio clonado, se llama halther:
  
  `cd C:\halther`

- Ahí  debes ver que existen algunos archivos y carpetas,
- Especialmente docker-compose.yml, ejecuta dir:
  `dir`

- Ahora ejecuta: (si falla es que no instalaste Docker-Desktop)
- 
docker pull graiionn/vue-frontend

docker pull graiionn/flask-backend

 - Esos archivos los va administrar Docker Desktop.
 - Ahora vamos a ajustar el docker-compose.yml:
 - Decide si quieres borrar su contenido, respaldarlo o reemplazarlo.
  
  debe tener exactamente esto:

```yaml
services:
  backend:
    image: graiionn/flask-backend
    container_name: flask-backend
    ports:
      - "5000:5000" # localhost:5000 asi entras
    volumes:
      - ./backend:/halther/backend 
    networks:
      - app-network

  frontend:
    environment:
      - NODE_ENV=${NODE_ENV}
    image: graiionn/vue-frontend
    container_name: vue-frontend
    ports:
      - "5173:5173"
      - "4173:4173"
      - "80:80"
      - "3000:3000"
    volumes:
      - ./backend:/halther/backend
    networks:
      - app-network
    depends_on:
      - backend
dos
networks:
  app-network:
    driver: bridge
```

 - Ya estás muy cerca.
 - En el mismo directorio que el .yml ejecuta:
  `docker-compose up`

 - Accede a http://localhost

### ¡LISTO!

 - Acabas de desplegar **super en fa** una aplicacion dockerizada y orquestada por Docker Compose, que está corriendo en producción!

 - Podrás verlo al usar tu navegador, abrir las ventana de desarrollo y ver la consola.
  
 - **El entorno de producción busca consumir de una base de datos en la nube así que si por alguna razón no conecta, significa que la instancia de base de datos no está operando y seguramente buscaremos una solución menos costosa y amigable en el futuro.**
  
 - No obstante a lo anterior, puedes probar el entorno de desarrollo usando los archivos que ya descargaste del repositorio: construir la app del backend usando python, construir la app del frontend usando Node.js con vite.
 - Es muy facil de hacer, tendremos el tutorial muy pronto:

**Obligatorio** - Instala Git para windows.
**Obligatorio** - Instala Docker Desktop
**Obligatorio** - Instala Node.js para windows
**Obligatorio** - Instala Python 13.12 para windows o superior.
Opcional - Instala Visual Studio Code