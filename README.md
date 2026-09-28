# fastapi crud through RestAPI

# FastAPI is a web framework for building HTTP-based service APIs in Python 3.8+. It uses Pydantic and type hints to validate serialize and deserialize data. 

# Pydantic is a data validation library for Python. While writing code in an IDE, Pydantic provides type hints based on annotations.


ex - from fastapi import FastAPI
from pydantic import BaseModel

# Uvicorn is a minimal low-level server/application web server for async frameworks
Technically, it implements a multi-process model with one main process, which is responsible for managing a pool of worker processes and distributing incoming HTTP requests to them.

# Asynchronous operations 
FastAPI's architecture inherently supports asynchronous programming. This design allows the single-threaded event loop to handle a large number of concurrent requests efficiently, particularly when dealing with I/O-bound operations like database queries or external API calls. For reference, see async/await pattern.

# Dependency Injection in FastAPI 
 FastAPI, dependency injection plays a pivotal role in optimizing the flexibility, testability, and overall architecture of applications.
 when there's a need to reuse code or override specific sections. Dependency injection in FastAPI facilitates these tasks seamlessly.
 It allows developers to declare components such as database sessions or authentication logic as function parameters. FastAPI automatically resolves these dependencies for each request, injecting the necessary instances.
 # Depends Function in FastAPI
 the Depends function is employed to manage dependency injection, serving as a common parameter for other functions.
 Syntax:
@app.get("URL"): Decorator specifying that the following function responds to HTTP GET requests at the specified URL.

