#%%
from ninjamongo.services.mongo_services import MongoService
service = MongoService("")
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
