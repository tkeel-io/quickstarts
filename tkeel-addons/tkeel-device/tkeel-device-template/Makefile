# ------------------------------------------------------------
# Copyright (c) Microsoft Corporation and TKEEL Contributors.
# Licensed under the MIT License.
# ------------------------------------------------------------
Binary ?= main
Image ?= tkeel-device-addons
GIT_COMMIT=$(shell git rev-parse HEAD)
GIT_BRANCH=$(shell git name-rev --name-only HEAD)
BUILD_DATE=$(shell date '+%Y-%m-%d-%H:%M:%S')
GIT_VERSION = $(shell git describe --always --abbrev=7 --dirty)


# docker tag
DOCKER_TAG ?= latest

################################################################################
# Go build details                                                             #
################################################################################
BASE_PACKAGE_NAME := github.com/tkeel-io/tkeel

DEFAULT_LDFLAGS:=-X $(BASE_PACKAGE_NAME)/pkg/version.GitCommit=$(GIT_COMMIT) \
  -X $(BASE_PACKAGE_NAME)/pkg/version.GitVersion=$(GIT_VERSION) \
  -X $(BASE_PACKAGE_NAME)/pkg/version.BuildDate=$(BUILD_DATE)


build_local:
	CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build  -ldflags="$(DEFAULT_LDFLAGS)" -o ./dist/linux_amd64/release/$(Binary)  ./main.go
	docker build -t tkeelio/$(Image):$(DOCKER_TAG) -f . .
	docker push  tkeelio/$(Image):$(DOCKER_TAG)

