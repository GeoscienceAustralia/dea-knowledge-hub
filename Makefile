# Build and run commands

run-local: # To run the site on your local computer (on Mac or Linux), use the command 'make'.
	make build-local
	make start-local

build-local: # This builds a local Docker container which runs 'make build' internally.
	docker build -t dea-knowledge-hub .

rebuild-local:
	docker build --no-cache -t dea-knowledge-hub .

start-local:
	docker run -it --rm --name dea-knowledge-hub --publish 8062:8062 --volume ./docs/notebooks:/docs/notebooks --volume ./output:/output --env-file .env dea-knowledge-hub \
	| grep --invert-match --regexp "WARNING.*Document headings start at" \
	| grep --invert-match --regexp "WARNING.*duplicate label" \
	| grep --invert-match --regexp "^copying images..." \
	| grep --invert-match --regexp ".*GET /_static.*" \
	| grep --invert-match --regexp ".*GET /_files.*" \
	| grep --invert-match --regexp ".*GET /_images.*"

build:
	sphinx-build -b dirhtml -j auto -a ./docs ./output

# Other commands

ssh:
	docker exec -it dea-knowledge-hub /bin/sh

test-redirects:
	npx mocha ./aws/cloudfront/functions/*.js

clean:
	rm -rf ./output
