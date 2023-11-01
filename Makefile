run:
	make build
	make start

build:
	docker build -t dea-docs .

start:
	docker run -it --rm --name dea-docs --publish 8011:8011 --volume ./docs:/docs --volume ./output:/output --env-file .env dea-docs \
		| grep --invert-match --regexp 'WARNING.*Document headings start at' \
		| grep --invert-match --regexp 'WARNING.*duplicate label'

rebuild:
	docker build --no-cache -t dea-docs .

ssh:
	docker exec -it --workdir /docs dea-docs /bin/sh
