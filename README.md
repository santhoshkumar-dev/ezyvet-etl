**ezyVet Data Engineer Test**


**Objective:**

Write a simple script to pipe data from the attached CSV into the MySQL tables provided

**Pre-requisites**

python 3.8 - ETL package, script and the tests are built using this version. 
For testing, docker is required to provision mysql 5.7.

**Project structure**

<code>

        ezyvet-etl
            ├── dist -> provides ezyvet_etl_santhosh-1.0.0 package for users to install in their environment)
            ├── docker-compose.yml -> provisions local mysql and adminer webserver to connect to mysql
            ├── Dockerfile
            ├── input
            ├── README.md
            ├── requirements.txt -> brings in python third party dependencies pandas, sqlalchemy etc
            ├── scripts -> python script which uses ezyvet_etl_santhosh-1.0.0 package built from src dir to ingest contacts file
            ├── setup.py -> package descriptor used to build ezyvet_etl_santhosh-1.0.0
            ├── src 
            ├── tests

</code>

**Implementation Overview**

python etl library (ezyvet_etl_santhosh) uses pandas to build contact, address and phone from the input csv file.

I have tried to use some of my recent python and docker knowledge to:
 - use pandas to analyse and transform data
 - demonstrate modular and object oriented programming 
 - build custom python package (ezyvet_etl_santhosh-1.0.0)
 - install this custom package and use it in the python script ingest_contact.py
 - provision local mysql and adminer for testing

**To test locally**

Install python3.8, docker, docker-compose.

Start mysql and adminer containers locally:

`cd ezyvet-etl`

`docker-compose up`

Create sample database and tables:


`docker exec -it ezyvet-etl_db_1 bash`

`mysql -pexample < /app/src/sql/schema.sql`

Once up, adminer web console will be available on http://localhost:8080 you can login as user root with password example

To execute ingest_contact.py, from project home directory:

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`pip install dist/ezyvet_etl_santhosh-1.0.0-py3-none-any.whl`

`./scripts/ingest_contact.py input/contact_list.csv`

**To do**

- Add more documentation
- Created some unit tests - add more tests to increase code coverage
- Create integration tests - I am new to docker, like to learn more before
- Refactor and optimize
- Handle SQL injection either using regex or third-party library
- Improve error handling
- Add logging
