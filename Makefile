dev-stack:
	docker compose up --build

dev-documentation:
	docker compose up --abort-on-container-exit --build documentation

dev-lock: dev-lock-sendria dev-lock-django dev-lock-documentation

dev-lock-documentation:
	docker compose rm -fsv documentation
	docker compose run --name $@ documentation poetry lock
	docker cp $@:/poetry.lock documentation/poetry.lock
	docker compose rm -fsv documentation

dev-lock-django:
	docker compose rm -fsv django
	docker compose run --name $@ django poetry lock
	docker cp $@:/poetry.lock django/poetry.lock
	docker compose rm -fsv django

dev-lock-sendria:
	docker compose rm -fsv sendria
	docker compose run --name $@ sendria poetry lock
	docker cp $@:/poetry.lock sendria/poetry.lock
	docker compose rm -fsv sendria

clean:
	docker compose down
	docker compose rm -fsv
