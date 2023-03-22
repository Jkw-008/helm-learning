from fastapi import FastAPI
import os
app = FastAPI()


@app.get("/")
async def root():
    return {"message": f"Hello World {os.getenv('person_name')}"}
