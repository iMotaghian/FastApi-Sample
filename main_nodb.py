from fastapi import FastAPI,HTTPException,status,Query,Path,Form,Body,File,UploadFile
from fastapi.responses import JSONResponse
from typing import Annotated,Optional,List
from contextlib import asynccontextmanager
import random

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


@app.get("/") # query
def name_list(q : str = Query(alias="search",description="can search",example="ali",default=None,max_length=50)): # def name_list(q : Annotated[str, Query(max_length=50)] = None ): # def name_list(q : Optional[str] = None) # def name_list(q : str | None = None)
    if q:
        return [ item for item in names_list if item["name"] == q ]
    return names_list

@app.get("/{id}") # path
def name(id:int = Path(alias="id alias",title="id",description="inja path ast")):
    for name in names_list:
        if name["id"] == id:
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")

@app.post("/",status_code=status.HTTP_201_CREATED) # body
def add_name(name:str = Body(embed=True)):
    temp = {"id":random.randint(6,100),"name":name}
    names_list.append(temp)
    return names_list

@app.put("/{id}",status_code=status.HTTP_200_OK) # form
def name_update(id:int = Path(),nname:str = Form(description="in form ast",default="mehrdad")):
    for name in names_list:
        if name["id"] == id:
            name["name"] = nname
            return name
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")

@app.delete("/{id}")
def delete_name(id:int):
    for name in names_list:
        if name["id"] == id:
            names_list.remove(name) 
            return JSONResponse(content={"details":"deleted"},status_code=status.HTTP_200_OK)
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")



@app.post("/upload_file/")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read() # Asynchronous reading
    return {"filename": file.filename, "content_type": file.content_type, "file_size": len(content)}

@app.post("/upload-multiple/")
async def upload_multiple(files: List[UploadFile]):
    return [
        {"filename": file.filename, "content_type": file.content_type}
        for file in files
    ]
