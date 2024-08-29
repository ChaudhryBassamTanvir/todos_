from fastapi import FastAPI # type: ignore
import uvicorn # type: ignore
from pydantic import BaseModel # type: ignore
app = FastAPI()

class Todo(BaseModel):
    id:int
    title:str
    

car:Todo={
    "id":1,
    "title":"bahs"
}

students =[{
    "userName":"Hashim Kardar",
    "age": 20,
},{
    "userName":"Haneen",
    "age": 20,
}]

@app.get("/student")
def getstudent(findName:str):
    for student in students:
        if student[ "userName" ] == findName:
            return student["age"]

    
    



@app.get("/addstudent")
def addstudent(userName:str,age:int):
    global students
    students.append({"userName":userName,"age":age})
    return students


@app.get("/gettodos")
def getTodos():
    print("Get Todos")
    return "get todos"

@app.post("/gettodos")
def getTodos():
    print(" post Get Todos")
    return "post method get todos"
    
    
@app.get("/getSingleTodos")
def getTodos(userName:str,rollNo:str):
    print( " Get single Todos ")
    return f"get single todos {userName} {rollNo} "


def start():
    uvicorn.run("todos.main:app", host="127.0.0.1", port=8000,reload=True)


 