###############################################################################
##  Name:   Dockerfile
##  Date:   2017-02-16
##  Developer:  Chris Page
##  Email:  christopher.page@ca.com
##  Purpose:   This Dockerfile contains the IoT example
################################################################################
#FROM container4armhf/armhf-alpine:3.5
# required for py-smbus
FROM container4armhf/armhf-alpine:edge

# Set the file maintainer (your name - the file's author)
MAINTAINER Page, Christopher T <Christopher.Page@ca.com>

# Set the application directory
WORKDIR /app

# Install dependencies for Cryptography
#RUN apk --update add build-base musl-dev libffi-dev openssl-dev python-dev py-pip

# Add CA Certificates for remote packages
#RUN apk add ca-certificates

# Install dependencies for Python Numpy
#RUN apk --update add build-base musl-dev linux-headers g++ python-dev py-pip

# Hack to get numpy installed: https://github.com/docker-library/python/issues/112
#RUN ln -s /usr/include/locale.h /usr/include/xlocale.h

# Add the testing repo
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

# Install dependencies for Python
RUN apk --update add build-base python-dev py-pip py-smbus@testing

# Install our requirements.txt
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

## Let's add all the examples into the /app directory for now
ADD . /app/.

CMD ["python", "app.py"]
#CMD ["ash"]
