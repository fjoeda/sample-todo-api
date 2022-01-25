# sample-todo-api

This is a sample todo API using Django-Ninja as the API framework and MongoDb for the database. It uses mongoengine to handle the connection with MongoDb database.

## How to run
1. Create .env file to save the python environment variable. More explanation here : https://code.visualstudio.com/docs/python/environments
2. Set the `MONGO_DB_URL` to your MongoDb Database Connection String.
3. Run the app using django runserver command.
`python ./manage.py runserver`
4. Access swagger-based documentation on `/todo-api/docs`
