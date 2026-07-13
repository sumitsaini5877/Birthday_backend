from fastapi import FastAPI
from app.api.routes import router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://birthdaygift-gamma-two.vercel.app","http://localhost:5500","http://127.0.0.1:5500"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)