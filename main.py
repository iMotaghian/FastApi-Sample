from fastapi import FastAPI

app = FastAPI()

# Hello world
# @app.get("/")
# def say_hello():
#     return {"Hello":"World"}


myList = [1,2,3,4,5,6,7,8,9,10]

@app.get("/about/{name}")
def aboutGetName(name:str):
    return {"data": name}