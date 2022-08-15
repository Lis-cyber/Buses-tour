# 🌄 Buses-Tour

Administrador de Agencia de Buses, que permite crear y editar buses, trayectos, conductores y pasajeros.

Para instalar y levantar el proyecto, se presenta la siguiente guía, tanto para el Back como para el front.

El primer paso es clonar el Repositorio (Allí estan ambas carpetas)
```bash
git clone https://github.com/Lis-cyber/Buses-tour.git
```

<br>
<br>

# 🌱 Back-End
- El primer paso es ingresar al repo previamente clonado, para ello abre una terminal e ingresa a la carpeta api

```bash
cd Buses-tour/api
```

- Procede a instalar las dependencias.

```bash
pip install -r requirements.txt
```
- Genera una Base de Datos en PostgreSQL (Debes tenerlo previamente instalado). Puedes hacerlo desde la terminal de SQL Shell con el siguiente comando, o ingresando al PGAdmin

```bash
CREATE DATABASE busses
```
- Ingresa a la carpeta config en el archivo settings.py, ubica la DATABASE y configura las credenciales con las de tu PostgreSQL.

```bash
'USER': '<user>',
'PASSWORD': '<password>',
```
- Ejecuta las migraciones
```bash
python manage.py migrate
```

- Y para completar el paso del Backend, ejecuta el siguiente comando para levantar el servidor.

```bash
python manage.py runserver
```

- Para acceder a la interfaz de Django REST framework, ingresa al siguiente path: 
```bash
http://127.0.0.1:8000/api/v1.0/
```

<br>
<br>

# 🌴 Front-End

- En una nueva terminal, ingresa al proyecto, a la carpeta client/
```bash
cd Buses-tour/client
```

- Procede a instalar las dependencias.

```bash
npm install
```
- En la raiz de la carpeta client, genera un archivo .env con la sigiente información.
```bash
BASE_URL=http://127.0.0.1:8000/api/v1.0/
```

- Finalmente ejecuta el siguiente comando para levantar el servidor.

```bash
npm run serve
```

<br>