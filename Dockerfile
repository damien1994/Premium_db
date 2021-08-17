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

#VOLUME ./data:/app/etl_premium_clients/db/output

# install dependencies
RUN make install

# run script
ENTRYPOINT ["etl_premium_clients"]
CMD [ "python", "-m" , "etl_premium_clients.main"]

#CMD ["etl_premium_clients", "(input_db)", "(input_table)", "(custom_path)", "(output_name_db)"]

# run script
#RUN etl_premium_clients --input_db db.db --input_table premium_payments --custom_path False --output_name_db db_transformed.sqlite3


#ENTRYPOINT ["premium"]
#CMD ["premium"]
#CMD make run