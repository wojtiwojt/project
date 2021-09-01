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

backend_attach:
	docker attach digital_desire_back

create_docs_as_html:
	@make  poetry_install
	docker-compose -f docker-compose.dev.yml exec backend poetry run make html -C docs/

poetry_install:
	docker-compose -f docker-compose.dev.yml exec backend poetry install