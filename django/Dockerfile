FROM ubuntu:21.10
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y python3 gcc g++ python3-dev musl-dev bash libffi-dev rustc cargo python3-wheel libssl-dev libz-dev libjpeg-dev libpng-dev python3-pip pkg-config libpq-dev
COPY poetry.lock pyproject.toml /app/
RUN pip install poetry
RUN poetry install --no-interaction
COPY . /app/
ENV PYTHONPATH=/app
CMD ["bash", "-c", "poetry run /app/manage.py migrate && poetry run /app/manage.py runserver 0.0.0.0:8012"]
