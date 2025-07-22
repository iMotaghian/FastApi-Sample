from fastapi import FastAPI, Depends
from pydantic import BaseModel,Field
from uuid import UUID
import models
from database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
# generate DB for first
models.Base.metadata.create_all(bind=engine)
# open DB and close DB function
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# Model class
class mySchoolClasses(BaseModel):
    name: str = Field(min_length=1)
    schoolName: str = Field(min_length=1,max_length=100)
    teacherName: str = Field(min_length=1,max_length=100)
    studentCount: int = Field(gt=1,lt=100) # gt greater than / lt ...

mySchoolClasses= []

@app.get("/")
def read_school_class(db: Session = Depends(get_db)):
    return db.query(models.mySchoolClasses).all()

# simple code old
myList = [1,2,3,4,5,6,7,8,9,10]    
# Hello world
@app.get("/hello/")
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