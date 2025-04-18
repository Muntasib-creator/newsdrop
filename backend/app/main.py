from fastapi import FastAPI
from app.api.news import router as news_router

app = FastAPI(
    title="NewsAPI",
    description="A FastAPI-based news aggregation service",
    version="1.0.0"
)

# Include routers
app.include_router(news_router)

@app.get("/")
async def root():
    return {"message": "Welcome to NewsAPI"}
