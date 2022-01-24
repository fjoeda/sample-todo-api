from ninja import NinjaAPI
from ninjamongo.services.mongo_services import MongoService
from ninjamongo.models.todo import CreateToDoBody, UpdateToDoBody
from ninjamongo.services.utls_service import print_response_json
from ninjamongo.controllers.controller_exception import ResourceNotFound, BadRequest
import os
service = MongoService(os.environ.get("MONGO_DB_URL"))

todo_api = NinjaAPI(
    title="Todo API",
    description="API for creating todo list"
)

# handling api exception
@todo_api.exception_handler(ResourceNotFound)
def resource_not_found(request, ex):
    return todo_api.create_response(
        request,
        print_response_json(404,"Resource not found"),
        status=404
    )

@todo_api.exception_handler(BadRequest)
def resource_not_found(request, ex):
    return todo_api.create_response(
        request,
        print_response_json(401,"Invalid input"),
        status=401
    )


# api routing
@todo_api.get('/todo/{todo_id}')
def get_todo(request, todo_id):
    try:
        todos = service.get_todo(todo_id)
        del todos['_id']
        return print_response_json(
            status = 200,
            message = 'OK',
            payload = todos
        ) 
    except:
        raise ResourceNotFound

@todo_api.get('/todo-raw/{todo_id}')
def get_todo_raw(request, todo_id):
    try:
        todos = service.get_todo_raw_id(todo_id)
        todos['_id'] = str(todos['_id'])
        return print_response_json(
            status = 200,
            message = 'OK',
            payload = todos
        ) 
    except:
        raise ResourceNotFound

@todo_api.get('/todo')
def get_all_todo(request):
    todos = service.get_all_todo()
    todos = [{key:item[key] for key in item.keys() if key != '_id'} for item in todos]
    return print_response_json(
        status = 200,
        message = 'OK',
        payload = todos
    )

@todo_api.get('/todo-raw')
def get_all_todo_raw(request):
    todos = service.get_all_todo()
    todo_list = []
    for item in todos:
        item['_id'] = str(item['_id'])
        todo_list.append(item)
    return print_response_json(
        status = 200,
        message = 'OK',
        payload = todo_list
    )

@todo_api.post('/todo/')
def create_todo(request, body:CreateToDoBody):
    try:
        service.create_todo(body.todo_item)
        return print_response_json(
            status = 200,
            message = 'Todo created',
        ) 
    except:
        raise BadRequest

@todo_api.post('/todo/{todo_id}')
def update_todo(request, todo_id, body:UpdateToDoBody):
    try:
        service.get_todo_raw_id(todo_id)
        service.edit_todo(todo_id,body.todo_item,body.is_done)
        return print_response_json(
            status = 200,
            message = 'Todo updated',
        ) 
    except:
        raise ResourceNotFound

@todo_api.delete('/todo/{todo_id}')
def delete_todo(request, todo_id):
    try:
        service.get_todo(todo_id)
        service.delete_todo(todo_id)
        return print_response_json(
            status = 200,
            message = 'Todo deleted',
        ) 
    except:
        raise ResourceNotFound