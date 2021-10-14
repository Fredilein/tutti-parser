# Tutti Parser

Get notified via Telegram Bot when a new product which potentially interests you is available on Tutti.

## Requirements
- Pipenv
- Python 3.x
- oder eifach docker

## Install & Run (Docker)
```
docker-compose up
```

## Installation (Old)
### MySql
- Start mysql service (e.g. via brew)
- Rename `example.connection.py` to `connection.py` and use own credentials
- Create SQL Tables and insert queries, use the code in `create_sql_tables` to do this.

### Telegram bot
- Register telegram bot (@BotFather)
- Rename `example.credentials.py` to `credentials.py` and use your bot-token

### Run
```
cd app
pipenv install -r requirements.txt
pipenv run python main.py
```
> Used pycharm for development: 
> Select pipenv and python interpreter (preferrably installed via brew) in run-configurations.

