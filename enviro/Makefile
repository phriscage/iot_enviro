default: run

run: build
	docker run -it --rm --privileged -v ${PWD}:/app --name iot_gpio-enviro phriscage/iot_gpio-enviro
build:
	docker build -t phriscage/iot_gpio-enviro .
