FROM ubuntu:21.10
WORKDIR /documentation
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
RUN apt update && apt install -y python3 gcc g++ python3-dev musl-dev bash libffi-dev rustc cargo python3-wheel libssl-dev libz-dev libjpeg-dev libpng-dev python3-pip
RUN pip install poetry
COPY poetry.lock pyproject.toml /documentation/
RUN poetry install --no-interaction
COPY . /documentation
ENTRYPOINT ["poetry", "run", "sphinx-autobuild", "/documentation", "/build", "--host", "0.0.0.0"]
