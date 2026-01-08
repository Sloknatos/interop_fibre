# Test technique
## Installation

-----------------------------------------------------------------------
### With Docker  
  

Go in the directory:
<div class="termy">

```console
cd interpro_fibre
```
Add env file:
<div class="termy">

```console
touch ./api/.env
```

</div>
Fill the variable like this :
<div class="termy">

```console
DATABASE_HOST=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_DB=
DATABASE_PORT=
SQLITE_PATH=[example: /home/.../interop_fibre/api/app/database/database.db]
```


Use docker-compose with the env you need (choice between `dev` or `prod`):
<div class="termy">

```console
docker-compose up -d --build [your_env_choice]
```

</div>
The prod environment expose 8443 port and the dev expose 8080.  

#### PROD
<a href=http://127.0.0.1:8443>backend address</a>  
<a href=http://127.0.0.1:8443/docs>Swagger address</a>

#### Dev  
<a href=http://127.0.0.1:8080>backend address</a>  
<a href=http://127.0.0.1:8080/docs>Swagger address</a>
  
You can run the test with:
<div class="termy">

```console
docker-compose up --build test
```

</div>
Wait few seconds and:
<div class="termy">

```console
docker-compose logs test
```

</div>

----------------------------------  

### Locally  
  

Go in the directory:
<div class="termy">

```console
cd interpro_fibre
```
Add env file:
<div class="termy">

```console
touch ./api/.env
```

</div>
Fill the variable like this :
<div class="termy">

```console
DATABASE_HOST=
DATABASE_USER=
DATABASE_PASSWORD=
DATABASE_DB=
DATABASE_PORT=
SQLITE_PATH=[example: /home/.../interop_fibre/api/app/database/database.db]
```

</div>

Install library
 <div class="termy">

```console
pip install -re requirements.txt
```

</div>
Poetry is not available as the pytest plugins seems to not be installed correctly, work in progress.

Launch the server:
</div>

Install library:
 <div class="termy">

```console
uvicorn --app-dir ./app main:app --host 0.0.0.0 --port 8080 --reload
```

</div>

#### Dev  
<a href=http://127.0.0.1:8080>Backend address</a>  
<a href=http://127.0.0.1:8080/docs>Swagger address</a>

You are able to launch tests simply like this:
 <div class="termy">

```console
pytest
```

</div>