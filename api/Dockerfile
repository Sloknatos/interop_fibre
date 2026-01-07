# Prepare an image for all stages
FROM python:3.12 as builder

WORKDIR /api
COPY ./pyproject.toml /api/pyproject.toml

RUN pip install -U pip setuptools poetry
RUN pip install fastapi["standard"]
ENV PYTHONPATH=/api

COPY ./app /api/app
COPY ./poetry.lock /api/poetry.lock


# Prepare image for running containers
FROM builder as runner

RUN pip install uvicorn["standard"]
RUN poetry install



# Create image for prod environment
FROM runner as prod

CMD ["uvicorn", "--app-dir", "/api/app", "main:app", "--host", "0.0.0.0", "--port", "8080"]


# Create image for dev environment
FROM runner as dev

RUN poetry install --with dev

CMD ["uvicorn", "--app-dir", "/api/app", "main:app", "--host", "0.0.0.0", "--port", "8080"]


# Create image for test
FROM builder as test

COPY ./app /api/test 
RUN poetry install --with test

CMD ["uvicorn", "--app-dir", "/api/app", "main:app", "--host", "0.0.0.0", "--port", "8080"]


# Create Database image
FROM postgres:latest as database

# Those lines should not exist like this in real life, I should use docker secret or other vault solution
# The purpose of those lines is to make the test review easier
# Never push sensitive data on version control !!

ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

EXPOSE 5432

