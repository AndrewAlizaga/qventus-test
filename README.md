# QVENTUS TEST - PARTS API
### this is a simple test API design to showcase best practices and regular conventions

## how to run 🚀

#### you have 2 paths to choose from, you can run the application locally natively or via docker.

## 1 - Local  🖥️

#### 1.1 - create your own virtual environment and install dependecies on requirements.txt
```bash
pip3 install -r ./requirements.txt
```

#### 1.2 - run the app 
```bash
uvicorn app.main:app --reload
```

### you are set! 

## 2 - Dockerize 🐳 (easiest alternative)

#### 2.1 - using docker compose
```bash
docker-compose up --build
```

## 3 - Test it out!
#### Once the app is running go to http://localhost:8000/docs to test out the features on the fastapi interactive docs or read the guidelines to do your own trials on postman/curl