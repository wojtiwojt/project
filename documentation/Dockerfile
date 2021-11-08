FROM alpine:3.14
WORKDIR /documentation
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing poetry  # switch to regular alpine when poetry is part of main
RUN apk add python3==3.9.5-r1 gcc python3-dev musl-dev bash
COPY poetry.lock pyproject.toml /documentation
RUN poetry install --no-interaction
COPY . /documentation
ENTRYPOINT ["poetry", "run"]
