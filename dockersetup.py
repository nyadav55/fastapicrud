# -------- docker fastapi - Python 3.14.5
To containerize your FastAPI application using Python 3.14 and Docker, 
you can use an optimized multi-stage or standard slim Docker setup.

# Step 1: Create a requirements.txt
Ensure your dependencies are saved in your project root. 
If you haven't generated it yet, run this inside your active virtual environment (env):

pip freeze > requirements.txt  

# Which one file should you use for Docker?
pip list                         
# those file name you got use it like The Clean & Minimal Approach (Recommended) paste in .txt file
fastapi
uvicorn
pydantic
# Now Use -  
pip freeze > requirements.txt

# Step 2: Create a Dockerfile - 
# Build the Docker image:
     docker build -t fastapicrud-app .
# Run the Docker container:
     docker run -d --name fastapicrud-container -p 8000:8000 fastapicrud-app
     docker compose up --build

# Step 3: Create a .dockerignore file
# To keep your container image clean and build fast, create a .dockerignore file in the root directory:
# Paste insde a file 
env/
__pycache__/
*.pyc
*.pyo
*.pyd
.git
.gitignore
.vscode/
Dockerfile
docker-compose.yml
README.md

# Step 4: Build and Run Your Docker Container
docker build -t fastapicrud-app .

# Run the Docker container:
docker run -d --name fastapicrud-container -p 8000:8000 fastapicrud-app

# You can now access your FastAPI app at http://localhost:8000 
# and the interactive API documentation at http://localhost:8000/docs.

# You can then run everything with a single command:
docker compose up --build

# Alternative: Using docker-compose.yml (orachestra) (Optional)

If you prefer managing your container via Docker Compose, create a docker-compose.yml in your root folder:
1. If you are using the Minimal Requirements (fastapi, uvicorn, pydantic)
Your existing docker-compose.yml will work without any changes. 
Pip will install those core tools and everything will boot up correctly.

2. Best Practice: Adding a Volume for Local Development
If you want your code changes on your Windows machine to reflect instantly inside the Docker container
 without having to rebuild the image every time, ensure your docker-compose.yml includes a volume mapping:
# paste inside YAML file 
version: '3.8'

services:
  web:
    build: .
    container_name: fastapicrud-container
    restart: always
    ports:
      - "8000:8000"
    volumes:
      - .:/app  # <--- This maps your local E:\git_ny_project\fastapicrud folder into the container
    command: uvicorn main:app --host 0.0.0.0 --port 8000 --reload

# Why use docker-compose.yml instead of plain docker run?
Saves typing: You don't have to remember long commands like docker run -d --name ... -p 8000:8000 ....

# One command startup: You just type docker compose up --build to build and launch everything.

# Easy scaling later: If you decide to add a database (like PostgreSQL or MongoDB) later on, 
you can add it right inside this file as a second service.

If error happens because a container named fastapicrud-container is already running 
or still exists from a previous docker run command. 
Docker containers need unique names.
# Solution 1 : Remove container_name from docker-compose.yml
you can open your docker-compose.yml and delete or comment out the container_name: line

# If port error means that port 8000 is already bound
# check port useage - Get-NetTCPConnection -LocalPort 8000
# Run - Stop-Process -Id <PID> -Force    press Ctrl + C in that terminal window

# Solution 2 : Change the Port in docker-compose.yml
Open your docker-compose.yml and change the ports line:

YAML
ports:
      - "8001:8000"  # Maps host port 8001 to container port 8000

#      Now Run - docker compose up --build

# Try these links in your browser:
API Home: http://localhost:8000

Interactive Docs (Swagger UI): http://localhost:8000/docs

Alternative Docs (ReDoc): http://localhost:8000/redoc