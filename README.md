# Greeting
Get greeting with your name
___

#### All necessary variables are stored in ***.env*** file in app top level directory
##### ***.env*** example
```
PORT=5000
SECRET_KEY = \xf8)\n\x05Z6i\n\x93\xcf\xe7\xa3{\xb6\x91 \xa7\xbf\xe1\xce\x12\x9e\xbf\x83
DB_HOST = db
DB_NAME = postgres
DB_USER = postgres
DB_PASS = 1234
DB_PORT = 5432
TEST_DB_HOST = db-test
TEST_DB_PORT = 5432
TEST_DB_NAME = postgres
```
#### To run app, in top level directory run:
```
docker-compose up
```

#### To run tests run in ***test/*** directory of app docker container:
```
pytest
```
___

### General overwiev
On home page you'll be asked to input your name
If your name was inputed for the first time you would get greeting message.
But if your name wasn't inputed for the first time you would get message that says that you've been already seen.
Also there is a button where you can see all the names that greeted
