from fastapi import FastAPI
from pydantic import BaseModel,Field
from uuid import UUID

app = FastAPI()
myList = [1,2,3,4,5,6,7,8,9,10]

# Model class
class mySchoolClasses(BaseModel):
    id: UUID
    name: str = Field(min_length=1)
    schoolName: str = Field(min_length=1,max_length=100)
    teacherName: str = Field(min_length=1,max_length=100)
    studentCount: int = Field(gt=1,lt=100) # gt greater than / lt ...
    
    
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

# DELETE method
@app.delete("/delete/{number:int}")
def deleteFromList(number:int):
    myList.remove(number)
    return {"List":myList}