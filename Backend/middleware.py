from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import EmailStr
app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)