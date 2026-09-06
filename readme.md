
### Installation & setup

1. Python version check
2. Install FastApi & Uvicorn
3. Venv setup
4. Project structure
6. First Fast api app


### Uvicorn is not exactly a FastAPI library. It is an ASGI server used to run FastAPI applications.

Think of it like this:

FastAPI → framework, where you write your API/routes.
Uvicorn is not exactly a FastAPI library. It is an ASGI server used to run FastAPI applications.

Think of it like this:

FastAPI → framework, where you write your API/routes.
Uvicorn → server, which runs your FastAPI application and handles HTTP requests.



run server with this command :
```
 uvicorn main:app --reload

```

Pydantic is a Python library that helps parse incoming data and provides validation

BaseModel is a class provided by Pydantic. By inheriting from BaseModel, we can define the structure of incoming request data and automatically validate that data.


## what is swagger UI


------------------------------------------------

## Lecture code - exceptionHandling.py

### httpException

 HTTPException is used to send an error response to the client.

 raise means stop the execution and send the error response to the client.


### custom exception

 a custom exception means an exception that you create yourself for a specific situation in your application.


--------------------------------------------------

# Global error handler
