# PIT STOP BLOG

### Descripcion:
Creacion de un miniblog desarrollado en Flask, utilizando las herramientas aprendidas en todo el año.

### Requisitos:
Para poder ejecutar nuestro proyecto, debe realizar los siguientes pasos:

1. Crear y activar un entorno Vitual.

`
python3 -m venv env
`

2. Clonar el repositorio.

`
git clone git@github.com:juanjcenturion/flask_practice1.git
`

3. Instalar requeriments.txt

` 
pip install -r requeriments.txt
`

4. Crear .env, utilizando .env.example como ejemplo


5. Migrar los modelos a una base de datos

` 
flask db init
flask db migrate -m "Mensaje de migracion"
flask db update
`

6. Correr la aplicacion de flask.

`
flask run --reload
`

### Thunder Client Consultas:
```
{
    "client": "Thunder Client",
    "collectionName": "miniblog_flask",
    "dateExported": "2023-11-07T23:16:31.357Z",
    "version": "1.1",
    "folders": [],
    "requests": [
        {
            "_id": "b25c3ebd-ad99-4bf1-90dc-76a79b319682",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/post",
            "url": "localhost:5000/post",
            "method": "GET",
            "sortNum": 10000,
            "created": "2023-11-07T22:53:56.042Z",
            "modified": "2023-11-07T22:53:56.042Z",
            "headers": [],
            "params": [],
            "tests": []
        },
        {
            "_id": "0a8b0567-d09d-454c-97a9-245aedd6f3f4",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/post",
            "url": "localhost:5000/post",
            "method": "POST",
            "sortNum": 20000,
            "created": "2023-11-07T22:57:31.656Z",
            "modified": "2023-11-07T22:57:31.656Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"title\":\"test_post\",\n  \"content\":\"Prueba de post de Publicaciones\",\n  \"date\":\"2023-11-07\",\n  \"author_id\":\"1\",\n  \"category_id\":\"1\"\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "a355d6d5-4afb-49d3-8c05-e6918737aac2",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/post/7",
            "url": "localhost:5000/post/7",
            "method": "PUT",
            "sortNum": 30000,
            "created": "2023-11-07T22:59:02.523Z",
            "modified": "2023-11-07T22:59:02.523Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"title\":\"cambio titulo metodo put\"\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "b69cb83b-8bf9-469a-bb79-7a2bc2abf0e2",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/post/7",
            "url": "localhost:5000/post/7",
            "method": "DELETE",
            "sortNum": 40000,
            "created": "2023-11-07T22:59:27.375Z",
            "modified": "2023-11-07T22:59:27.375Z",
            "headers": [],
            "params": [],
            "tests": []
        },
        {
            "_id": "8b77366b-dec8-42ad-9e95-c96517569343",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/user",
            "url": "localhost:5000/user",
            "method": "POST",
            "sortNum": 50000,
            "created": "2023-11-07T23:01:24.805Z",
            "modified": "2023-11-07T23:01:24.805Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"username\":\"juanc-admin\",\n  \"password_hash\":\"juan1234\",\n  \"is_admin\": true\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "cb3e9547-3c25-4c7f-b2f1-0ed875906cfe",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/user/9",
            "url": "localhost:5000/user/9",
            "method": "PUT",
            "sortNum": 60000,
            "created": "2023-11-07T23:02:27.432Z",
            "modified": "2023-11-07T23:02:27.433Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"password_hash\":\"juan12345\"\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "74df0b80-8b56-4675-a1b8-d42a0e68517a",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/user/6",
            "url": "localhost:5000/user/6",
            "method": "DELETE",
            "sortNum": 70000,
            "created": "2023-11-07T23:03:15.652Z",
            "modified": "2023-11-07T23:03:15.652Z",
            "headers": [],
            "params": [],
            "tests": []
        },
        {
            "_id": "ecb9d172-3ea8-4235-930e-daf23ca829db",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/login",
            "url": "localhost:5000/login",
            "method": "GET",
            "sortNum": 80000,
            "created": "2023-11-07T23:04:39.640Z",
            "modified": "2023-11-07T23:04:39.640Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"username\":\"juanc-admin\",\n  \"password\":\"juan12345\"\n}",
                "form": []
            },
            "tests": []
        },
        {
            "_id": "591ee327-0c5c-410d-a830-b3f70d2ad278",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/user",
            "url": "localhost:5000/user",
            "method": "GET",
            "sortNum": 90000,
            "created": "2023-11-07T23:05:18.731Z",
            "modified": "2023-11-07T23:05:18.731Z",
            "headers": [],
            "params": [],
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "c1c6d527-df97-4202-a265-0acb514fedde",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/user/5",
            "url": "localhost:5000/user/5",
            "method": "GET",
            "sortNum": 100000,
            "created": "2023-11-07T23:05:32.048Z",
            "modified": "2023-11-07T23:05:32.048Z",
            "headers": [],
            "params": [],
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "3b20340b-dc6e-4d12-abad-cc3b759d961b",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/category",
            "url": "localhost:5000/category",
            "method": "GET",
            "sortNum": 110000,
            "created": "2023-11-07T23:06:21.810Z",
            "modified": "2023-11-07T23:06:21.810Z",
            "headers": [],
            "params": [],
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "1fa643d1-17e8-4b38-98d1-5f43f3e9a6a1",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/category/1",
            "url": "localhost:5000/category/1",
            "method": "GET",
            "sortNum": 120000,
            "created": "2023-11-07T23:06:37.046Z",
            "modified": "2023-11-07T23:06:37.046Z",
            "headers": [],
            "params": [],
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "5eb2ec0e-f080-4550-9982-70d97ebc9dbd",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/category",
            "url": "localhost:5000/category",
            "method": "POST",
            "sortNum": 130000,
            "created": "2023-11-07T23:07:40.835Z",
            "modified": "2023-11-07T23:07:40.835Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"name\":\"TC\"\n}",
                "form": []
            },
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "99b5c2e6-9aab-4ac3-a581-57d366e5f8fa",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/category/7",
            "url": "localhost:5000/category/7",
            "method": "PUT",
            "sortNum": 140000,
            "created": "2023-11-07T23:08:31.433Z",
            "modified": "2023-11-07T23:08:31.433Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"name\":\"Turismo Carretera\"\n}",
                "form": []
            },
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "342bb394-340e-40d4-ba5f-12ebbab22f7e",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/category/5",
            "url": "localhost:5000/category/5",
            "method": "DELETE",
            "sortNum": 150000,
            "created": "2023-11-07T23:09:37.355Z",
            "modified": "2023-11-07T23:09:37.355Z",
            "headers": [],
            "params": [],
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "c898d88e-f9e8-4dbc-b285-b6a8d40c70b0",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/comment",
            "url": "localhost:5000/comment",
            "method": "POST",
            "sortNum": 160000,
            "created": "2023-11-07T23:15:38.029Z",
            "modified": "2023-11-07T23:15:38.029Z",
            "headers": [],
            "params": [],
            "body": {
                "type": "json",
                "raw": "{\n  \"content\":\"prueba post comentario\",\n  \"date\":\"2023-11-07\",\n  \"author_id\":3,\n  \"post_id\":6\n}",
                "form": []
            },
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        },
        {
            "_id": "6fa0f4fe-f43f-4268-b671-64bfd4620714",
            "colId": "fdf84712-f6a2-4ebf-83d8-176143bb6e4f",
            "containerId": "",
            "name": "localhost:5000/comment/15",
            "url": "localhost:5000/comment/15",
            "method": "DELETE",
            "sortNum": 170000,
            "created": "2023-11-07T23:16:20.931Z",
            "modified": "2023-11-07T23:16:20.931Z",
            "headers": [],
            "params": [],
            "auth": {
                "type": "bearer",
                "bearer": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTM5ODI2OSwianRpIjoiYTA4YjYwN2UtNzYxNS00YWRjLTllNTItZWJiZmRmZmNmNzBiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6Imp1YW5jLWFkbWluIiwibmJmIjoxNjk5Mzk4MjY5LCJleHAiOjE3MDAyNjIyNjksImlzX2FkbWluIjpudWxsfQ.Y4SynVdfBpy9-43OJhJL4tutB7kTeNy5f5-jZbnkoMQ"
            },
            "tests": []
        }
    ]
}
```