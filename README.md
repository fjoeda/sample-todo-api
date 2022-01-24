# sample-todo-api

This is a sample todo API using Django-Ninja as the API framework and MongoDb for the database. It uses mongoengine to handle the connection with MongoDb database.

## How to run
1. Create .env file and set the `MONGO_DB_URL` to your MongoDb Database Connection String.
2. Run the app using django runserver command.
`python ./manage.py runserver`
3. Access swagger the documentation on `/todo-api/docs`
