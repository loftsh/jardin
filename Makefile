
build:
	docker-compose build

up: build
	docker-compose up -d

logs:
	docker-compose logs -f

.PHONY: up logs build
