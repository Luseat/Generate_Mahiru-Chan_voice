from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.voice_routes import router as voice_router

app = FastAPI(
    title="Mahiru~Chan Voice",
    description="API for Mahiru Shiina Voice Generation (T2V & V2V)",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(voice_router, prefix="/api/v1")


@app.get("/")
async def root():
    return{
        "message": "Welcome to Mahiru~Chan Voice API",
        "status": "running",
        "Waifu": "Mahiru Shiina"
    }