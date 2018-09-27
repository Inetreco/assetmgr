#! /bin/bash

echo "removing containers and images"
docker-compose rm
docker image rm $(docker image ls -a -q)
docker rm $(docker ps -a -q)
echo "removing all migrations"
rm  -f `find . -name "0001*"`
rm  -f `find . -name "0002*"`
rm  -f `find . -name "0003*"`
rm  -f `find . -name "0004*"`
rm  -f `find . -name "0005*"`
rm  -f `find . -name "0006*"`
rm  -f `find . -name "0007*"`
rm  -f `find . -name "0008*"`
rm  -f `find . -name "0009*"`
echo "rebuilding docker"
docker-compose up --build
