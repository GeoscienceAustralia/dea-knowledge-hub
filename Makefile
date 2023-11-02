run:
	make build
	make start

build:
	docker build -t dea-docs .

rebuild:
	docker build --no-cache -t dea-docs .

start:
	docker run -it --rm --name dea-docs --publish 8011:8011 --volume ./docs/notebooks:/docs/notebooks --volume ./output:/output --env-file .env dea-docs

ssh:
	docker exec -it dea-docs /bin/sh
