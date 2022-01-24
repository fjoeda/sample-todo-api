from mongoengine import Document, fields
import datetime
import random
from ninja import Schema

class ToDo(Document):
    todo_id = fields.StringField(default=f"todo-{random.randint(10000,999999)}", unique=True)
    todo = fields.StringField(required = True)
    is_done = fields.BooleanField(required=True, default=False)
    created_at = fields.DateField(default=datetime.datetime.utcnow())


class CreateToDoBody(Schema):
    todo_item:str

class UpdateToDoBody(Schema):
    todo_item:str = None
    is_done:bool = None