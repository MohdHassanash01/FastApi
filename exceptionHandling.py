
# httpException

# HTTPException is used to send an error response to the client.

# raise means stop the execution and send the error response to the client.


# custom exception

# a custom exception means an exception that you create yourself for a specific situation in your application.


# Global error handler


#------------------------------------------------

# httpException

from fastapi import FastAPI, status, HTTPException, Request 
from fastapi.responses import JSONResponse


app = FastAPI()


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




# custom exeption

class UserNotFoundException(Exception):
    def __init__(self, name):
       self.name = name


@app.exception_handler(UserNotFoundException)
def user_not_found_handler(request: Request, exc: UserNotFoundException):
    return JSONResponse(
        status_code=404,
        content={
            "status":"error",
            "message" : f"User {exc.name} not found"
        }
    )


@app.get("/user/{username}")
def get_user(username: str):
    if username != "mohit":
        raise UserNotFoundException(username)
    return {
        "name" : username
    }