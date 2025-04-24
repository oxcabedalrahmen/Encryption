from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import se

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class Input(BaseModel):
    mass:str


name=""
x=""
v=""
v1=""
@app.post("/encrypt")
async def i1(data:Input):
    global name
    global x
    name=data.mass

    
    if not name.strip():  
        x="note text"
    else:
        x=se.cy(name)
   

        
    return {"ok":"ok"}
@app.post("/up")
async def up(data:Input):
        global v
        global v1
        v = data.mass
        if not v.strip():
          v1="note text"
        else:
          v1=se.de(v)
        return {"ok":"up"}

     

@app.get("/")
def  good():
    return {"mass":x,
            "da":v1         
            }
