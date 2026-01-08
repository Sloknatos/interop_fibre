# Prepare an image for all stages
FROM python:3.12 as builder

WORKDIR /api
COPY ./requirements.txt /api/requirements.txt
COPY ./.env /api/.env

RUN pip install -U pip setuptools
RUN pip install fastapi["standard"]
ENV PYTHONPATH=/api
RUN pip install -r requirements.txt

COPY ./app /api/app


# Prepare image for running containers
FROM builder as runner

RUN pip install uvicorn["standard"]



# Create image for prod environment
FROM runner as prod

CMD ["uvicorn", "--app-dir", "/api/app", "main:app", "--host", "0.0.0.0", "--port", "8080"]


# Create image for dev environment
FROM runner as dev


CMD ["uvicorn", "--app-dir", "/api/app", "main:app", "--host", "0.0.0.0", "--port", "8080"]


# Create image for test
FROM builder as test

COPY ./ /api/

CMD ["pytest"]
