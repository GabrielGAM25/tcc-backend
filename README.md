
## Required software

[Python 3.8.2](https://www.python.org/)

## Setup instructions

Run `pip install -r requirements.txt` to install required libraries

Create a `.env` file (copy it from `.env.example`)

Run `docker-compose up -d` to install PostgreSQL and PgAdmin4

#### If you need to install any python package, please add it to `requirements.txt` so that we can keep track of our dependencies

## Available scripts
<h3><code>flask db:seed</code></h3>
Populates the database with mock data
<h3><code>flask db:clear</code></h3>
Deletes all the records in the database
<h3><code>flask db migrate</code></h3>
Compares the models present in the API with the database structure and generates a new migration script based on the diff
<h3><code>flask db upgrade</code></h3>
Run all pending migrations
<h3><code>flask db downgrade</code></h3>
Execute last migration script's <code>downgrade</code> function
