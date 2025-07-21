from fastapi import FastAPI

app = FastAPI()

# Hello world
@app.get("/")
def say_hello():
    return {"Hello":"World"}