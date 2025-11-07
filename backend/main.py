from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend origin or ["*"] while dev
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PostureData(BaseModel):
    user_id: str
    exercise: str
    posture_score: float
    reps: int

data_store: List[PostureData] = []

@app.post("/posture")
def save_posture(data: PostureData):
    data_store.append(data)
    return {"message": "Data saved", "count": len(data_store)}

@app.get("/posture")
def get_posture():
    return data_store
