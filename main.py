
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






