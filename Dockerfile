# set base image
FROM python:3.8-alpine

# set work direction
WORKDIR /app

# add make to python alpine image
RUN apk add --update make

# # copy the content of the local src directory to the working directory
ADD requirements.txt ./
RUN apk add gcc musl-dev libffi-dev && \
    pip install -U  cffi pip setuptools && \
    pip3 install --no-cache-dir -r requirements.txt

ADD MANIFEST.in ./
ADD README.md ./
ADD setup.py ./
ADD etl/ ./etl
ADD Makefile ./

# install dependencies
RUN make install

# run script
RUN make run

# command to run on container start
#CMD [ "hacktoberfest_jems"]