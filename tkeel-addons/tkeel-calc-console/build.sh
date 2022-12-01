#!/bin/bash
PWD=`pwd`

CONTAINER_CLI?=docker

${CONTAINER_CLI} docker build -t tkeelio/tkeel-calc-console:latest -f ${PWD}/Dockerfile ${PWD}/
${CONTAINER_CLI} docker push tkeelio/tkeel-calc-console:latest
