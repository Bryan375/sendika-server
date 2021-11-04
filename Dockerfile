# FROM python:3.7-alpine3.14
FROM python:3.7-buster

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

RUN pip install --upgrade pip

RUN pip install pipenv

# ENV PROJECT_DIR /app

# WORKDIR ${PROJECT_DIR}}

# RUN python3.7 -m pip install https://files.pythonhosted.org/packages/71/c4/ce24841375cf4393787dbf9a645e271c19a03d2d9a0e5770b08ba76bcfde/dgl-0.6.1-cp37-cp37m-manylinux1_x86_64.whl

WORKDIR /app
# COPY requirements.txt /app/requirements.txt

COPY Pipfile* /app

RUN pipenv lock --keep-outdated --requirements > /app/requirements.txt
RUN set -ex && pip install --no-cache-dir -r /app/requirements.txt 



# RUN set -ex && pip install --upgrade pip && pip install --no-cache-dir -r /app/requirements.txt
# RUN set -ex && pipenv install --system --deploy

ADD . .

# EXPOSE 8000

WORKDIR /app/sendika_server

# CMD ["gunicorn", "--bind", ":8001", "--workers", "3", "sendika_server.wsgi:application"]
CMD gunicorn sendika_server.wsgi:application --bind 0.0.0.0:$PORT