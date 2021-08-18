# set base image
FROM python:3.8

# set work direction
WORKDIR /app

# # copy the content of the local src directory to the working directory
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

COPY MANIFEST.in ./
COPY README.md ./
COPY setup.py ./
COPY etl_premium_clients/ ./etl_premium_clients
COPY Makefile ./


# install dependencies
RUN make install

# run script
#ENTRYPOINT ["etl_premium_clients"]
ENTRYPOINT [ "python", "-m" , "etl_premium_clients.main"]