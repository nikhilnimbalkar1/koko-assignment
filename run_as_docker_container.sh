#!/bin/sh
docker build -t koko-assignment -f Dockerfile .
docker tag  koko-assignment:latest  koko-assignment:main
docker compose up

