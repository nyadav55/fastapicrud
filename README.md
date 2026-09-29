# fastapi crud through RestAPI

# FastAPI is a web framework for building HTTP-based service APIs in Python 3.8+. It uses Pydantic and type hints to validate serialize and deserialize data. 

# Pydantic is a data validation library for Python. While writing code in an IDE, Pydantic provides type hints based on annotations.

ex - from fastapi import FastAPI
     from pydantic import BaseModel

# Uvicorn is a fast, lightweight ASGI (Asynchronous Server Gateway Interface) web server implementation for Python.
Technically, it implements a multi-process model with one main process, which is responsible for managing a pool of worker processes and distributing incoming HTTP requests to them.

# Asynchronous operations 
FastAPI handles asynchronous operations by running async def endpoints directly on the main event loop using Python's asyncio, allowing your server to pause during slow tasks and handle other incoming requests, particularly when dealing with I/O-bound operations like database queries or external API calls. For reference.

# Dependency Injection in FastAPI 
 FastAPI, dependency injection plays a pivotal role in optimizing the flexibility, testability, and overall architecture of applications.
 when there's a need to reuse code or override specific sections. Dependency injection in FastAPI facilitates these tasks seamlessly.
 It allows developers to declare components such as database sessions or authentication logic as function parameters. FastAPI automatically resolves these dependencies for each request, injecting the necessary instances.
 # Depends Function in FastAPI
 the Depends function is employed to manage dependency injection, serving as a common parameter for other functions.
 Syntax:

# Decorater operations 
FastAPI (like @app.get("URL") or @app.post("URL")) map HTTP methods and URL paths to specific Python functions.
