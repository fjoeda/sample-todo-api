from mongoengine import connect
from ninjamongo.models.todo import ToDo
from bson.objectid import ObjectId
import os

class MongoService():
    def __init__(self,host) -> None:
        connect(host = host)

    def create_todo(self, todo_item):
        todo = ToDo()
        todo.todo = todo_item
        todo.save()

    def get_todo(self, id):
        todo_item = ToDo.objects(todo_id = id).as_pymongo()
        return todo_item[0]

    def get_todo_raw_id(self, id):
        id = ObjectId(id)
        todo_item = ToDo.objects(id = id).as_pymongo()
        return todo_item[0]

    def edit_todo(self, id, todo_desc = None, todo_status = None):
        #todo_item = ToDo.objects(todo_id = id)
        id = ObjectId(id)
        if todo_desc != None:
            ToDo.objects(id = id).update_one(todo = todo_desc)
        
        if todo_status != None:
            ToDo.objects(id = id).update_one(is_done = todo_status)

    def get_all_todo(self):
        return ToDo.objects.as_pymongo()
        

    def delete_todo(self,id):
        todo_item = ToDo.objects(todo_id = id)
        todo_item.delete()

    
