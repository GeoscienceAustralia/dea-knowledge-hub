docker build -t dea-docs .

rem docker rm dea-docs || true

docker run -it --name dea-docs --publish 8011:8011 --volume .\content:\docs\content --env-file .env dea-docs
