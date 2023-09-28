#!/bin/bash

COMMAND="$1"

case $COMMAND in

    build)
        docker build -t dea-docs .
        ;;

    rebuild)
        docker build --no-cache -t dea-docs .
        ;;

    start)
            docker rm dea-docs || true
            docker run \
                -it \
                --name dea-docs \
                --publish 8011:8011 \
                --volume ./content:/docs/content \
                --env-file .env \
                dea-docs
        ;;

    ssh)
        docker exec -it --workdir /docs dea-docs /bin/sh
        ;;

    *)
        ./make.sh build
        ./make.sh start
        ;;
esac
