run:
	make build
	make start

build:
	docker build -t dea-docs .

rebuild:
	docker build --no-cache -t dea-docs .

start:
	docker run -it --rm --name dea-docs --publish 8011:8011 --volume ./output:/output --env-file .env dea-docs \
		| grep --invert-match --regexp 'WARNING.*Document headings start at' \
		| grep --invert-match --regexp 'WARNING.*duplicate label'
