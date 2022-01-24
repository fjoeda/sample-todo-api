FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV MONGO_DB_URL=<Your_mongo_db_url>
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["manage.py","runserver","0.0.0.0:8080"]