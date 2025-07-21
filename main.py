from fastapi import FastAPI

app = FastAPI()
myList = [1,2,3,4,5,6,7,8,9,10]

# Hello world
@app.get("/")
def say_hello():
    return {"Hello":"World"}

# get with value
@app.get("/about/{name}")
def aboutGetName(name:str):
    return {"data": name}

# get list
@app.get("/myList/")
def getList():
    return {"List":myList}

# post method:
@app.post("/add/{number:int}")
def addToList(number:int):
    myList.append(number)
    return {"List":myList}

# PUT method
@app.put("/updatelist/{index:int}")
def updateList(index:int, newNumber:int):
    myList[index] = newNumber
    return {"UpdatedList":myList}