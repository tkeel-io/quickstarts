#!/bin/bash
PWD=`pwd`

docker build -t tkeelio/tkeel-calc-mul:latest -f ${PWD}/Dockerfile ${PWD}/
docker push tkeelio/tkeel-calc-mul:latest