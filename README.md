# Premium_db

A sqlite database which contains premium payments. Each row corresponds to a monthly payment.

By creating a python class with 3 methods (download_data, process_data, save_data), try to create a new database where data structure allows to find easily churn on products or new subscribers

## Some explanations on repo

### Quick description of the repo
- The ETL process is executed in etl_premium_clients.main.py: [here](etl_premium_clients/main.py)
- Main script calls PerformETL python class which executes load, transform and extract functions: [here](etl_premium_clients/PerformETL.py)
- The output of the ETL process is stored in [here](etl_premium_clients/db/output/db_transformed.sqlite3)
- Logs of main execution are stored : [here](etl_premium_clients/logs/etl.log)
- Some tests are stored: [here](etl_premium_clients/tests/test_perform_etl.py)
- ETL process can be executed in a docker container. The dockerfile: [here](Dockerfile)
- Check data folder [here](data) where sqlite output is persisted when script is run into container
- Metabase (GUI) has been plug on output database : you can access on localhost after starting docker-compose

### Some tips on repo
- If you decide to run locally the script without specifiyng custom args, you can use the 'make run' command
- Otherwise, you can specify your own arguments described in utils script : [here](etl_premium_clients/utils.py)

## Running files

### Run with docker

```bash
# build etl process image (not pushed in dockerhub yet)
docker build . -t etl_process -f Dockerfile
# run etl process into docker container with default args
docker run -v $(PWD)/data:/app/etl_premium_clients/db/output etl_process

# to run metabase and see some analytics KPI
docker-compose -up
http://localhost:3000/
```


### Local development
Python >= 3.8

```bash
virtualenv -p python3.8 venv
source venv/bin/activate
pip3 install -r requirements.txt

# Local run 
make run (takes default values)
or 
python -m etl_premium_clients \
    --input_db <path to input db> \
    --input_table <name of sqlite table> \
    --custom_path <True or False - Always true if you define your own path to db> \
    --output_name_db <name of db transformed (output of ETL process)>
    
# Local linter
make linter

# Local test
make tests
```

## References
- [Github repos](https://github.com/iamaziz/etl/blob/master/pipeline.py)

## TO DO
- deals with volume for etl sqlite container
- add logs for unit test
- add unit test for load and extract steps
- add github actions