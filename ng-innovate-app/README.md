# NG Innovation Day Micro-services Demo App

A simple micro-services application with datastore. The goal is to demonstrate application lifecycle management with project Keswick and micro-services visualisation with project Trinidad.

## Develeopment Env Setup

Create a user-defined bridge network

```bash
docker network create ng-innovate-net
```

### Setup a PostgreSQL Docker Container

```bash
docker pull postgres:latest
docker run --network ng-innovate-net --name ng-innovate-db -e POSTGRES_PASSWORD=mysecretpassword -d -p 5432:5432 postgres:latest
docker exec -it my-postgres-container /bin/bash
psql -U postgres
CREATE DATABASE mydatabase;
\c mydatabase
CREATE TABLE "user" (
    id serial PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL
);
\q
exit
```

This will pull the latest PostgreSQL image, create a container named "ng-innovate-db," and expose port 5432 for database connections.

### Create and run app API micro service

```bash
cd ./app
docker build . -t dcauldwell/ng-innovate-app:0.0
docker run --network ng-innovate-net --name ng-innovate-app -d -p 4000:5000 dcauldwell/ng-innovate-app:0.0
```

This will create an image, create a container named "ng-innovate-app" and expose internal port 5000 as external port 4000 for API connections.

### Test the API accepts GET and POST methods and communicate with DB

Create a user:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"john_doe"}' http://localhost:4000/users
```

Retrieve the user list:

```bash
curl http://localhost:4000/users
```

```bash
docker run -it --entrypoint=/bin/bash ng-innovate-app /bin/bash 
```

### Create and run app UI micro service

```bash
cd ./ui
docker build . -t dcauldwell/ng-innovate-ui:0.0
docker run --network ng-innovate-net --name ng-innovate-ui -d -p 4001:5000 dcauldwell/ng-innovate-ui:0.0
```

Retrieve the UI:

```bash
curl http://localhost:4001
```
