SHELL := /bin/bash

default: run

run:
	docker-compose -f docker-compose.yml up -d

log:
	docker-compose -f docker-compose.yml logs -f

clean:
	docker-compose -f docker-compose.yml stop && docker-compose -f docker-compose.yml 

build:
	docker-compose -f docker-compose.build.yml build

deploy:
	docker deploy -c docker-compose.yml iot_enviro
