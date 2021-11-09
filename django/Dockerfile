FROM alpine:3.14
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing poetry  # switch to regular alpine when poetry is part of main
RUN apk add python3==3.9.5-r1 python3-dev py3-pip gcc pkgconfig postgresql-dev musl-dev bash
COPY poetry.lock pyproject.toml /app/
# RUN poetry config virtualenvs.create false && 
RUN poetry install --no-interaction
COPY . /app/
ENV PYTHONPATH=/app
CMD ["bash", "-c", "poetry run /app/pozabanka/manage.py migrate && poetry run /app/pozabanka/manage.py runserver 0.0.0.0:8012"]
