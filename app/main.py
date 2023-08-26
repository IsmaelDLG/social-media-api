from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import engine
from . import models
from .routers import posts, users, votes, auth

# alembic handles this
# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"data": "hello world!"}

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(votes.router)
app.include_router(auth.router)