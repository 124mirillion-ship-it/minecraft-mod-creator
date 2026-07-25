from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import dimensions, translations, mods, versions

app = FastAPI(
    title="Minecraft Mod Creator API",
    description="AI-powered Minecraft Mod Creator with multi-language support",
    version="0.1.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(dimensions.router, prefix="/api/dimensions", tags=["Dimensions"])
app.include_router(translations.router, prefix="/api/translations", tags=["Translations"])
app.include_router(mods.router, prefix="/api/mods", tags=["Mods"])
app.include_router(versions.router, prefix="/api/versions", tags=["Versions"])

@app.get("/api/health")
async def health_check():
    return {"status": "ok", "message": "Minecraft Mod Creator API is running"}

@app.get("/")
async def root():
    return {"message": "Welcome to Minecraft Mod Creator API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
