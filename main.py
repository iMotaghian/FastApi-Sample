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

mySchoolClassesList = []

@app.get("/")
def read_school_class(db: Session = Depends(get_db)):
    return db.query(models.mySchoolClasses).all()


@app.post("/")
def create_school_class(mySchoolClass: mySchoolClasses, db: Session = Depends(get_db)):
    school_class = models.mySchoolClasses()

    school_class.name = mySchoolClass.name
    school_class.schoolName = mySchoolClass.schoolName
    school_class.teacherName = mySchoolClass.teacherName
    school_class.studentCount = mySchoolClass.studentCount
    # Let's commit the changes ...
    db.add(school_class)
    db.commit()

@app.put("/{schoolclass_id}")
def schoolClassUpdate(mySchoolClass_id:int ,mySchoolClass:mySchoolClasses, db: Session = Depends(get_db)):
    school_class = db.query(models.mySchoolClasses).filter(models.mySchoolClasses.id == mySchoolClass_id).first()
    if school_class is None:
        print("The school Class is not Exsist !")
    school_class.name = mySchoolClass.name
    school_class.schoolName = mySchoolClass.schoolName
    school_class.teacherName = mySchoolClass.teacherName
    school_class.studentCount = mySchoolClass.studentCount
    
    db.add(school_class)
    db.commit()

    return mySchoolClass

@app.delete("/{schoolclass_id}")
def delete_school_class(mySchoolClass_id:int , db: Session = Depends(get_db)):
    school_class = db.query(models.mySchoolClasses).filter(models.mySchoolClasses.id == mySchoolClass_id).first()

    if school_class is not None:
        db.query(models.mySchoolClasses).filter(models.mySchoolClasses.id == mySchoolClass_id).delete()

        db.commit()

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