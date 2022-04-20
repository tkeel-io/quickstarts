#!/bin/bash
PWD=`pwd`

docker build -t tkeelio/tkeel-calc-add:latest -f ${PWD}/Dockerfile ${PWD}/
docker push tkeelio/tkeel-calc-add:latest