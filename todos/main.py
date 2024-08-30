from fastapi import FastAPI,Body,Query,Path # type: ignore
import uvicorn # type: ignore
from pydantic import BaseModel# type: ignore
from typing import Annotated

app = FastAPI()

class Todo(BaseModel):
    id:int
    title:str
    
class User(BaseModel):
     userName:str
     userDescription:str
    

car:Todo={
    "id":1,
    "title":"bahs"
}


@app.get("/MainRoute")
def  MainRoute(item:Annotated[int,Body()]): #Body saying k item integer type hai or body parameter hai ap ne value query me receive ni karni
    result = item.dict()  #although poor format we use pandyntic
    return result   
  
  
 #by default 
@app.get("/ParamRoute")  #in first we define types but in second we can define conditions
def  ParamRoute(item:Annotated[str,Query(max_length=10,min_length=4)]):  
    return item 

@app.get("/Pattern")                                                        #start from fix and than a letters caps or num
def  ParamRoute(item:Annotated[str,Query(max_length=10,min_length=4,pattern="^fix[a-zA-Z0-9]")]):  
    return item 

#work with body parameter
@app.get("/Path/{id}")  #gt greater than,,,, ge greater than or equal, lt lessthan 
def  Path(id:Annotated[int,Path(le=5 , ge=3 )]):  
    return id

#agr ek hai tu key nahi banni pre ge wo object direct ho ga lekin agr 2 hain tu keyt banni pre ge 
@app.get("/item")
def item(item:Todo ,user:User):
    print(user)
    return item



@app.get("/item2")
def item(item:Todo ,user:User,count:Annotated[int,Body()]):
    print(user)
    return item



@app.get("/servermain/{id}/assignment/{assignment_id}")  # type: ignore
def MainRoute(id: int, assignment_id: int, query: str, id_num: int,item:Todo):
  return item
    # return {
    #     "message": "Server is up and running",
    #     "id num": id_num,
    #     "query": query,
    #     "than my dynamic id": id,
    #     "than dynamic assignid": assignment_id
    # }


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


                