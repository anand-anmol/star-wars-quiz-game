#!/bin/bash

docker build -t star-wars-receiver ./receiver/.
docker build -t star-wars-storage ./storage/.
docker build -t star-wars-ui ./ui/.