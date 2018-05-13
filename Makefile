
build: Dockerfile
	docker-compose build

up: build
	docker-compose up -d

logs:
	docker-compose logs -f

lint:
	docker-compose exec web flake8 .

test: lint

.PHONY: up logs build test lint
