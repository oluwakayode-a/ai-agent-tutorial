from fastapi import FastAPI
import os

app = FastAPI()

name = os.environ.get("MY_PROJECT")

@app.get("/")
def read_index():
    return {"msg": name}