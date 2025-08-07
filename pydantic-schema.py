from fastapi import FastAPI,HTTPException,status,Query,Path,Form,Body,File,UploadFile
from fastapi.responses import JSONResponse
from typing import Annotated,Optional,List
from contextlib import asynccontextmanager
import random
from pydantic import BaseModel

@asynccontextmanager # @app.on_event("startup")
async def lifespan(app: FastAPI):
    print("Application startup")
    yield 
    print("Application shutdown")

app = FastAPI(lifespan=lifespan)

names_list = [
    {"id":1, "name":"ali"},
    {"id":2, "name":"maryam"},
    {"id":3, "name":"arousha"},
    {"id":4, "name":"aziz"},
    {"id":5, "name":"zahra"},
]

class PersonCreateSchema(BaseModel):
    name : str
    
class PersonResponseSchema(BaseModel):
    id : int
    name : str

@app.get("/",response_model=List[PersonResponseSchema]) 
def name_list(q : str = Query(alias="search",description="can search",example="ali",default=None,max_length=50)): # def name_list(q : Annotated[str, Query(max_length=50)] = None ): # def name_list(q : Optional[str] = None) # def name_list(q : str | None = None)
    if q:
        return [ item for item in names_list if item["name"] == q ]
    return names_list

@app.post("/",status_code=status.HTTP_201_CREATED,response_model=PersonResponseSchema) 
def add_name(person : PersonCreateSchema):
    temp = {"id":random.randint(6,100),"name":person.name}
    names_list.append(temp)
    return temp
