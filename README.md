# ApiReservaHabitacionesTuG

## Descripcion

La API REST Reservas de Habitaciones es una API REST que permite la reserva de habitaciones, registro de usuarios y creacion de habitaciones.
Existe dos usuarios `admin` y `cliente`:

## Requisitos

- Python
- Django
- Django Rest Framework
- MySQL
- Docker (opcional, solo si se desea ejecutar en un contenedor)
- Docker Compose (opcional, solo si se desea ejecutar en un contenedor)

## Configuración del Proyecto

El proyecto utiliza Django Rest Framework y se puede ejecutar en un contenedor de Docker junto con MySql. A continuación, se detallan los pasos para configurar el proyecto:

1. Clona este repositorio en tu máquina local.

   `git clone https://github.com/MartinAAcebeyL/ApiReservaHabitacionesTuG.git`
2. Asegúrate de tener Docker instalado en tu máquina.
3. En la raíz del proyecto, ejecuta el siguiente comando para construir las imágenes de Docker:

   `docker-compose build`
4. Entra a la imagen de Docker de la base de datos:

   `docker-compose run db sh`
5. Una vez dentro de la imagen de Docker de la base de datos, ejecuta el siguiente comando para crear la base de datos:

   `mysql -u root -p`
6. Cuando se te solicite una contraseña, ingresa `root`. Luego, ejecuta el siguiente comando para crear la base de datos:

   `CREATE DATABASE hotelTuG;`

4. Una vez que se hayan creado las imágenes, ejecuta el siguiente comando para iniciar los contenedores:

   `docker-compose up`

5. Una vez que los contenedores se hayan iniciado correctamente, podrás acceder a la API en http://localhost:8000/api/.

---

## Ejemplos de Consumo de la API

Se adjunta una [carpeta](./examples/) con ejemplos en formato JSON que contiene ejemplos de solicitudes para cada uno de los endpoints utilizando Postman. Puedes importar este archivo en Postman para probar los endpoints y ver los resultados.

## Ejecución de Pruebas y Coverage
1. docker-compose up
2. docker-compose exec backend sh
3. cd HotelTuG/
4. python manage.py test apps
5. coverage run --source='.' manage.py test apps
6. coverage report
7. coverage html

# Endpoints

## Clientes

- **Registro de Cliente (POST /api/clientes/)**

  Este endpoint permite registrar un nuevo cliente. Se deben proporcionar todos los campos requeridos, incluyendo nombre, apellido, correo electrónico y contraseña. El cliente se crea con éxito y se devuelve la información del cliente registrado.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "nombre": "lucas",
    "apellido": "lucas",
    "ci": 123456,
    "email": "luis@gmail.com",
    "password": 123456,
    "fecha_nacimiento": "2000-11-30"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": "45312be5-2d7b-4df0-a019-24c44056d464",
    "last_login": null,
    "nombre": "lucas",
    "apellido": "lucas",
    "ci": 123456,
    "email": "luis@gmail.com",
    "password": "pbkdf2_sha256$600000$DKgetQCKXtIlXWpxCIGfug$PxqdDwvw05jBiJYEckirNYjP3w0tQowHqb0AddhxObA=",
    "fecha_nacimiento": "2000-11-30",
    "fecha_registro": "2023-07-10",
    "is_staff": false,
    "is_superuser": false,
    "is_active": true
  }
  ```

- **Inicio de Sesión (POST /api/login/)**

  Este endpoint permite a un cliente iniciar sesión. Se deben proporcionar el correo electrónico y la contraseña del cliente. Si las credenciales son válidas, se generará un par de tokens de acceso y actualización JWT y se devolverá en la respuesta.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "email": "luis@gmail.com",
    "password": "123456"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "message": "Login successfully",
    "success": true,
    "data": {
      "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTY4OTg0LCJpYXQiOjE2ODg5Njg2ODQsImp0aSI6IjBlYzNiZTI3ZGVhZDQ2MWU5NGQzN2QxYjBiNjM2ZjkwIiwidXNlcl9pZCI6IjQ1MzEyYmU1LTJkN2ItNGRmMC1hMDE5LTI0YzQ0MDU2ZDQ2NCJ9.HCiUqJDzufV35pMo2OkldkO87qrz-U-fBITTccizTqM",
      "refresh-token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTA1NTA4NCwiaWF0IjoxNjg4OTY4Njg0LCJqdGkiOiJmZGJjYmJhMzM5ZmU0NmFkOWI3YTRmMzRmNDVlOWRlZiIsInVzZXJfaWQiOiI0NTMxMmJlNS0yZDdiLTRkZjAtYTAxOS0yNGM0NDA1NmQ0NjQifQ.ucgT4fzKAd7gpHPumObtOQUtBjIHxUj4pGlkbn6hxUE"
    }
  }
  ```

- **Cierre de Sesión (POST /api/logout/)**
  Este endpoint permite a un cliente cerrar sesión. Se debe proporcionar el token de actualización JWT en el cuerpo de la solicitud. El token de actualización se invalidará y el cliente se desconectará.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "refresh_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4OTA1NTE5MywiaWF0IjoxNjg4OTY4NzkzLCJqdGkiOiJhYjJjMWUyZGUwYWY0N2Q5OTMyMGM0YTIzMDE1YzM2MiIsInVzZXJfaWQiOiI0NTMxMmJlNS0yZDdiLTRkZjAtYTAxOS0yNGM0NDA1NmQ0NjQifQ.3f924ggh14gBxo9wZv51mM3tZp3z2lU3CpLyBYLAp-E"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "message": "Session ended successfully",
    "success": true
  }
  ```

- **Listar Clientes (GET /api/clientes/)**

  Este endpoint permite listar todos los clientes registrados en el sistema. Solo se puede acceder a este endpoint si se tiene el permiso de autenticación.

  **Cuerpo de la Solicitud:**

  ```json
  {}
  ```

  **Cuerpo de salida:**

  ```json
  [
  {
      "id": "02ec90e207d8428ebf8b57d2bfcfd482",
      "last_login": null,
      "nombre": "Martin",
      "apellido": "Acebey",
      "ci": 123456,
      "email": "martin@gmail.com",
      "password": "pbkdf2_sha256$600000$3j4lZIJpgFBjhzBddKJKqk$5mzwAtKsvGJhDYCOCnhKjM2FOBlEcDMD1yQ+oWASzgE=",
      "fecha_nacimiento": "2000-11-30",
      "fecha_registro": "2023-07-09",
      "is_staff": false,
      "is_superuser": false,
      "is_active": true
  },
  {
      ...
  }
  ]
  ```

- **Obtener Detalles del Cliente (GET /api/clientes/{id}/)**

  Este endpoint permite obtener los detalles de un cliente específico identificado por su ID. Solo se puede acceder a este endpoint si se tiene el permiso de autenticación.

  **Cuerpo de la Solicitud:**

  ```json
  {}
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": "02ec90e207d8428ebf8b57d2bfcfd482",
    "last_login": null,
    "nombre": "Martin",
    "apellido": "Acebey",
    "ci": 123456,
    "email": "martin@gmail.com",
    "password": "pbkdf2_sha256$600000$3j4lZIJpgFBjhzBddKJKqk$5mzwAtKsvGJhDYCOCnhKjM2FOBlEcDMD1yQ+oWASzgE=",
    "fecha_nacimiento": "2000-11-30",
    "fecha_registro": "2023-07-09",
    "is_staff": false,
    "is_superuser": false,
    "is_active": true
  }
  ```

- **Actualizar Detalles del Cliente (PUT /api/clientes/{id}/)**

  Este endpoint permite actualizar los detalles de un cliente específico identificado por su ID. Solo se puede acceder a este endpoint si se tiene el permiso de autenticación. Se pueden modificar campos como nombre, apellido, correo electrónico, etc.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "nombre": "Martin 123456",
    "apellido": "Acebey",
    "ci": 123456,
    "email": "martin123@gmail.com",
    "password": 123456,
    "fecha_nacimiento": "2000-11-30"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": "45312be5-2d7b-4df0-a019-24c44056d464",
    "last_login": null,
    "nombre": "Martin 123456",
    "apellido": "Acebey",
    "ci": 123456,
    "email": "martin123@gmail.com",
    "password": "123456",
    "fecha_nacimiento": "2000-11-30",
    "fecha_registro": "2023-07-10",
    "is_staff": false,
    "is_superuser": false,
    "is_active": true
  }
  ```

- **Eliminar Cliente (DELETE /api/clientes/{id}/)**

  Este endpoint permite eliminar un cliente específico identificado por su ID. Solo se puede acceder a este endpoint si se tiene el permiso de autenticación. El cliente se eliminará permanentemente del sistema.

  **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json

  ```

## Habitaciones

- **Listar Todas las Habitaciones (GET /api/habitaciones/)**

  Este endpoint permite listar todas las habitaciones del hotel. Devuelve una lista de todas las habitaciones con sus detalles.
  **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json
  [
  {
      "id": 9,
      "numero": "246",
      "piso": "4",
      "precio": "173.81",
      "estado": true,
      "descripcion": "After majority forward open student establish.",
      "tipo": "Su"
  },{ ...}
  ]

  ```

- **Listar Habitaciones Disponibles (GET /api/habitaciones/disponibles)**

  Este endpoint permite listar todas las habitaciones disponibles en el hotel. Se pueden aplicar filtros opcionales para el precio máximo y los tipos de habitación. Devuelve una lista de las habitaciones disponibles que cumplen con los filtros.

  **URL**: /api/habitaciones/disponibles?precio_max=200&tipo[]=S&tipo[]=D

  **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json
  [
    {
      "id": 1,
      "numero": 101,
      "piso": 1,
      "precio": "100.00",
      "estado": true,
      "descripcion": "Habitación individual",
      "tipo": "S"
    },
    {
      "id": 2,
      "numero": 201,
      "piso": 2,
      "precio": "150.00",
      "estado": true,
      "descripcion": "Habitación doble",
      "tipo": "D"
    }
  ]
  ```

- **Obtener Detalles de una Habitación (GET /api/habitaciones/{id})**

  Este endpoint permite obtener los detalles de una habitación específica identificada por su ID. Devuelve la información detallada de la habitación.

  **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": 1,
    "numero": 101,
    "piso": 1,
    "precio": "100.00",
    "estado": true,
    "descripcion": "Habitación individual",
    "tipo": "S"
  }
  ```

- **Crear una Habitación (POST /api/habitaciones/admin/crear/)**

  Este endpoint permite crear una nueva habitación. Solo los administradores tienen acceso a este endpoint. Se deben proporcionar todos los campos necesarios, como el número de habitación, el piso, el precio, la descripción y el tipo de habitación. Devuelve los detalles de la habitación creada.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "numero": 301,
    "piso": 3,
    "precio": "200.00",
    "estado": true,
    "descripcion": "Habitación matrimonial",
    "tipo": "M"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": 3,
    "numero": 301,
    "piso": 3,
    "precio": "200.00",
    "estado": true,
    "descripcion": "Habitación matrimonial",
    "tipo": "M"
  }
  ```

- **Actualizar una Habitación (PUT /api/habitaciones/admin/{id}/)**

  Este endpoint permite actualizar los detalles de una habitación específica identificada por su ID. Solo los administradores tienen acceso a este endpoint. Se pueden modificar campos como el número de habitación, el piso, el precio, la descripción y el tipo de habitación. Devuelve los detalles de la habitación actualizada.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "precio": "180.00",
    "estado": false
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": 2,
    "numero": 201,
    "piso": 2,
    "precio": "180.00",
    "estado": false,
    "descripcion": "Habitación doble",
    "tipo": "D"
  }
  ```

- **Eliminar una Habitación (DELETE /api/habitaciones/admin/{id}/)**

  Este endpoint permite eliminar una habitación específica identificada por su ID. Solo los administradores tienen acceso a este endpoint. La habitación se eliminará permanentemente del sistema

  **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json
  {
    "message": "Habitación eliminada exitosamente",
    "success": true
  }
  ```

## Reservas

- **Listar Reservas (GET /api/reservas/)**

    Este endpoint permite obtener la lista de todas las reservas realizadas. Devuelve una lista de todas las reservas con sus detalles.

    **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json
  [
    {
      "id": 1,
      "habitacion": 101,
      "fecha_inicio": "2023-07-10",
      "fecha_fin": "2023-07-15",
      "cliente": 1,
      "monto": "500.00",
      "metodo_pago": "Tarjeta de Crédito",
      "estado": "Pendiente"
    },
    {
      "id": 2,
      "habitacion": 201,
      "fecha_inicio": "2023-07-12",
      "fecha_fin": "2023-07-16",
      "cliente": 2,
      "monto": "700.00",
      "metodo_pago": "Efectivo",
      "estado": "Pagado"
    }
  ]
  ```

- **Obtener Detalles de una Reserva (GET /api/reservas/{id})**

  Este endpoint permite obtener los detalles de una reserva específica identificada por su ID. Devuelve la información detallada de la reserva.

  **Cuerpo de la Solicitud:**

  ```json

  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": 1,
    "habitacion": 101,
    "fecha_inicio": "2023-07-10",
    "fecha_fin": "2023-07-15",
    "cliente": 1,
    "monto": "500.00",
    "metodo_pago": "Tarjeta de Crédito",
    "estado": "Pendiente"
  }
  ```

- **Crear una Reserva (POST /api/reservas/crear/)**

  Este endpoint permite crear una nueva reserva de habitación. Se deben proporcionar los detalles de la reserva, como la habitación, las fechas de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago. La API valida los datos de la reserva y asigna automáticamente el estado correspondiente (Pendiente, Pagado o Eliminado). Devuelve los detalles de la reserva creada.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "habitacion": 301,
    "fecha_inicio": "2023-07-20",
    "fecha_fin": "2023-07-25",
    "cliente": 3,
    "monto": "900.00",
    "metodo_pago": "Transferencia Bancaria"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": 3,
    "habitacion": 301,
    "fecha_inicio": "2023-07-20",
    "fecha_fin": "2023-07-25",
    "cliente": 3,
    "monto": "900.00",
    "metodo_pago": "Transferencia Bancaria",
    "estado": "Pendiente"
  }
  ```

- **Actualizar una Reserva (PUT /api/reservas/admin/{id}/)**

  Este endpoint permite actualizar los detalles de una reserva existente identificada por su ID. Solo los administradores tienen acceso a este endpoint. Se pueden modificar campos como la habitación, las fechas de estadía, los datos de facturación e identificación del cliente, el monto pagado y el método de pago. La API valida los datos de la reserva y actualiza el estado en consecuencia. Devuelve los detalles de la reserva actualizada.

  **Cuerpo de la Solicitud:**

  ```json
  {
    "fecha_inicio": "2023-07-14",
    "fecha_fin": "2023-07-18",
    "monto": "600.00",
    "metodo_pago": "Tarjeta de Crédito"
  }
  ```

  **Cuerpo de salida:**

  ```json
  {
    "id": 2,
    "habitacion": 201,
    "fecha_inicio": "2023-07-14",
    "fecha_fin": "2023-07-18",
    "cliente": 2,
    "monto": "600.00",
    "metodo_pago": "Tarjeta de Crédito",
    "estado": "Pendiente"
  }
  ```
