# pull official base image
FROM python:3.9.7

# set work directory
WORKDIR /backend_docker

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV POETRY_VERSION=1.1.8
# install psycopg2 dependencies

RUN pip install "poetry==$POETRY_VERSION"
COPY poetry.lock pyproject.toml /backend_docker/
RUN poetry config virtualenvs.create false && poetry install --no-interaction

COPY . /backend_docker

CMD ["bash", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8012"]