
import requests
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message":"hello world"}


@app.get("/about")
def about():
    return { "message": "this is about page"}


@app.get("/users")
def users():
    return {
        "users":[
            "hassan",
            "ashraf",
            "lolopolo"
        ]
    }



# dynamic parameters

@app.get("/user/{userId}")
def getuser(userId: int): #  automatic type validation provided by FastAPI using Python type hints.  

    print({"userid"  : userId})
    res = requests.get(f"https://jsonplaceholder.typicode.com/posts/{userId}")

    data = res.json()

    return {
        "message": "user data",
        "data" : data
    }



# query parameters

# browser url : http://127.0.0.1:8000/add?a=12&b=13

@app.get("/add")
def query_params(a:int,b:int = 13): # default params
    return {
        "sum is" : a + b
    }



# multiple query parameters

from typing import Optional

# username can be a str OR it can be None.

@app.get("/userDetail")
def query_params(
    username: Optional[str] = None,
    email: Optional[str] = None,
    password: Optional[str] = None
    ): 

    if not username or  not email or not password:
        return {
            "message": "credential is required..."
        }

    return {
        "message": "Credentials received",
        "username": username,
        "email": email,
        "password": password
    }



# post method


from pydantic import BaseModel

class Address(BaseModel):
    city: str

class User(BaseModel):
    username: str
    password: str
    address : Address

@app.post("/create-user")
def createuser(user: User):
    return {
        "username": user.username,
        "password": user.password,
        "address": user.address
    }
