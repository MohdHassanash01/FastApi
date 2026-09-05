# 59:49 - 

from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Todos(BaseModel):
    id : int
    title : str
    description : str
    completed : bool



todos = []


# health check api

@app.get("/")
def func():
    return {
        "message" : "hello from fast api"
    }




# create todos 

@app.post("/create-todo")
def getRoute(todo: Todos):

    todos.append(todo)

    print(todos)

    return {
        "message" : "todo created successfully",
        "data" : todo
    }




# get todos

@app.get("/todos")
def get_todos():

    if len(todos) < 1:
        return {
            "message": "todos don't exists"
        }
    
    return {
        "message" : "fetch all todos",
        "data" : todos
    }



# get single todo

@app.get("/todo/{todoId}")
def getTodo(todoId: int):
    for todo in todos:
        if todo.id == todoId:
           return todo
    return {
        "error": "Todo not found"
    }     



# update todo


@app.put("/todo/{todoId}")
def update_Todo(todoId:int,data: Todos):
    for index,todo in enumerate(todos):
        if todo.id == todoId:
            todos[index] = data

            return {
                "message": "Todo updated successfully",
                "data": data
            }

    return {
         "message": "todo not found"
     }     



# delete todo

@app.delete("/todo/{id}")
def delete_todo(id:int):
    for index, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(index)
            return {
                "message": "Data deleted",
            }
    return {
        "message": "todo not found"
    }    




# mix all inputs from user
# means - path params + query params + req body  

class User(BaseModel):
    username : str
    email : str
    password : str 


class UserResponce(BaseModel):
    username : str
    email : str


users = []

@app.post("/user")
def createuser(user: User):
    users.append(user)
    return {
        "message" : "user created",
        "data": user
    }



@app.put("/users/{userId}")
def update_user(userId: int,data: User,notify: bool = False):
    for index, user in enumerate(users):
        if user.id == userId:
            users[index] = data 
            return {
                "message" : "user updated",
                "notify" : notify,
                "data" : data
            }
    else:
        return {
            "message": "user not found"
        }   



# responce model

# response validation
# hide sensitive data
# output formatting

@app.get("/users",response_model=UserResponce)
def getusers():
    return {
        "username" : "lolopolo",
        "email" : "lolopolo@gmail.com",
        "password" : "cmdkscmkd" 
    }




# http status code


@app.post("/create", status_code=status.HTTP_201_CREATED)
def create():
    return {
        "message": "user created"
    }


# error handle

@app.get("/user-exam/{id}")
def get_user(id:int):
    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {
        "id" : 1,
        "username": "hassan ashraf"
    }



# exception handling.py
