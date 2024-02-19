from fastapi import FastAPI
from edit_db import router as edit_router



app = FastAPI(title="College Grades Project")
app.include_router(edit_router) 

@app.get("/")
async def get_start():
    return {"hello":'world'}