# Premium_db

A sqlite database which contains premium payments. Each row corresponds to a monthly payment.

By creating a python class with 3 methods (download_data, process_data, save_data), try to create a new database where data structure allows to find easily churn on products or new subscribers

## References
- [Github repos](https://github.com/iamaziz/etl/blob/master/pipeline.py)
- [Sqlite tutorial](https://www.sqlitetutorial.net/sqlite-python/creating-database/)

## TO DO
- improve dependencies by declaring only necessary repos (done)
- change make run in dockerfile for etl process (prevents arguments cli from being taken into account)
- deals with volume for etl sqlite container
- add logs
- add lint and hint
- add unit test for function (ongoing)
- add to try microservices like GUI or API and manage them with docker compose
- add docker (ongoing)
- add github actions
- add metabase for data exposition