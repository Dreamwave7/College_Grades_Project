from fastapi import FastAPI


app = FastAPI(title="College Grades Project")

@app.get("/")
async def get_start():
    return {"hello":'world'}