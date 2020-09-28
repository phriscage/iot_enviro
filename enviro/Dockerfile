###############################################################################
##  Name:   Dockerfile
##  Date:   2020-09-26
##  Developer:  Chris Page
##  Email:  phriscage@gmail.com
##  Purpose:   This Dockerfile contains the IoT example
################################################################################
# required for py-smbus
FROM arm32v7/alpine:3.12

# Set the file maintainer (your name - the file's author)
MAINTAINER Chris Page <phriscage@gmail.com>

# Set the application directory
WORKDIR /app

# Install dependencies for Cryptography
#RUN apk --update add build-base musl-dev libffi-dev openssl-dev python-dev py-pip

# Add CA Certificates for remote packages
#RUN apk add ca-certificates

# Install dependencies for Python
RUN apk --update add build-base python3 python3-dev py3-pip py3-smbus py3-wheel && \
	ln -fs /usr/bin/python3 /usr/bin/python

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Cleanup 
RUN apk del build-base && \
  	rm -rf /var/cache/apk/*

## Let's add all the examples into the /app directory for now
ADD . /app/.

CMD ["python", "app.py"]
