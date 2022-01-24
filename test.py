#%%
from ninjamongo.services.mongo_services import MongoService
service = MongoService("mongodb+srv://fatur:fatur@cluster0.jmwhf.mongodb.net/todoCollection?retryWrites=true&w=majority")
# %%
service.create_todo("cek 3")
# %%
service.get_all_todo()
# %%
for item in service.get_all_todo():
    print(item.todo_id)
    print(item.todo)
# %%
service.edit_todo('todo-249174','mengubah')
# %%
service.delete_todo('todo-249174')
# %%
service.get_todo('todo-863434')

# %%
service.get_todo_raw_id()