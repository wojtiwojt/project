FROM alpine:3.14
WORKDIR /
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing poetry  # switch to regular alpine when poetry is part of main
RUN apk add python3==3.9.5-r1 gcc python3-dev musl-dev bash
COPY poetry.lock pyproject.toml /
RUN poetry install --no-interaction
CMD ["poetry", "run", "sendria", "--db", "/db", "--http-ip", "0.0.0.0", "--http-port", "80"]
