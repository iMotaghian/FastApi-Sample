from fastapi import FastAPI,HTTPException,status
import random
app = FastAPI()

names_list = [
    {"id":1, "name":"ali"},
    {"id":2, "name":"maryam"},
    {"id":3, "name":"arousha"},
    {"id":4, "name":"aziz"},
    {"id":5, "name":"zahra"},
]

@app.get("/")
def name_list():
    return names_list

@app.get("/{id}")
def name(id:int):
    for name in names_list:
        if name["id"] == id:
            return name
    return HTTPException(detail={"not found"},status_code=status.HTTP_404_NOT_FOUND)

@app.post("/")
def add_name(name:str):
    temp = {"id":random.randint(6,100),"name":name}
    names_list.append(temp)
    return names_list

@app.put("/{id}")
def name_update(id:int,nname:str):
    for name in names_list:
        if name["id"] == id:
            name["name"] = nname
            return name
    return HTTPException(detail={"not found"},status_code=status.HTTP_404_NOT_FOUND)

@app.delete("/")
def delete_name(id:int):
    for name in names_list:
        if name["id"] == id:
            names_list.remove(name) 
            return "deleted"
    return HTTPException(detail={"not found"},status_code=status.HTTP_404_NOT_FOUND)
