from fastapi import FastAPI
import Schema
import models
from database import wngine,SessionLocal
from

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World mai hu giyan"}

@app.post("/blog")
def create_blog(blog: Schema.Blog):
    return {"Blog": f"this is my first blog with tittle {blog.title}"}


