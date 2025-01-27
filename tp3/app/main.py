from fastapi import FastAPI
from app.auth.api.endpoints import router as auth_router
from app.files.api.endpoints import router as files_router
from database import init_db
from app.database import init_db

app = FastAPI()

# Registrar routers
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(files_router, prefix="/files", tags=["Files"])


@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to the API"}
