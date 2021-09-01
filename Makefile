build:
	docker-compose -f docker-compose.dev.yml  build

clean:
	docker-compose -f docker-compose.dev.yml down -v

run:
	docker-compose -f docker-compose.dev.yml up --build

makemigrations:
	docker-compose -f docker-compose.dev.yml exec backend python3 manage.py makemigrations

migrate:
	docker-compose -f docker-compose.dev.yml exec backend python3 manage.py migrate

collectstatic:
	docker-compose -f docker-compose.dev.yml run backend python manage.py collectstatic

setup:
	@make clean
	@make build
	@make run
	@make makemigrations
	@make migrate
	@make collectstatic

up:
	docker-compose -f docker-compose.dev.yml up -d

backend_attach:
	docker attach backend_desire

blint:
	docker-compose -f docker-compose.dev.yml exec backend isort -c core apps tests
	docker-compose -f docker-compose.dev.yml exec backend black core apps tests --check

blint-fix:
	docker-compose -f docker-compose.dev.yml exec backend isort apps core apps tests
	docker-compose -f docker-compose.dev.yml exec backend black core apps tests

btest-t:
	docker-compose -f docker-compose.dev.yml exec -T backend pytest

create_docs_as_html:
	@make  poetry_install
	docker-compose -f docker-compose.dev.yml exec backend poetry run make html -C docs/

poetry_install:
	docker-compose -f docker-compose.dev.yml exec backend poetry install

poetry_lock:
	docker-compose -f docker-compose.dev.yml exec backend poetry lock --no-update

# Example of use
# make poetry_add package="black"

poetry_add:
	docker-compose -f docker-compose.dev.yml exec backend poetry add $(package)

poetry_remove:
	docker-compose -f docker-compose.dev.yml exec backend poetry remove $(package)

poetry_lock_add:
	@make poetry_add package=$(package)
	@make poetry_lock


# python-decouple