from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import model
from database import engine
from routers import users,auth_routes




app = FastAPI()
model.Base.metadata.create_all(bind=engine)

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
    
app.include_router(users.router)
app.include_router(auth_routes.router)



