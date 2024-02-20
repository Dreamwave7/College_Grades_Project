from fastapi import FastAPI
from edit_db import router 


app = FastAPI(title="College Grades Project")
app.include_router(router) 

@app.get("/")
async def get_start():
    return {"hello":'world'}