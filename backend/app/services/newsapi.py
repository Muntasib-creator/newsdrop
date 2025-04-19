import httpx
from fastapi import HTTPException
from app.settings import settings
from app.logger import logger

NEWS_API_URL = "https://newsapi.org/v2"

async def fetch_news(q: str = "the-verge", page: int = 1, pageSize: int = 10):
    logger.info(f"Fetching news for query: {q}, page: {page}, pageSize: {pageSize}")
    ENDPOINT = "/everything"
    url = f"{NEWS_API_URL}{ENDPOINT}"
    headers = {
        "X-Api-Key": settings.news_api_key,
    }
    params = {
        "q": q,
        "page": page,
        "pageSize": pageSize,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)

    if response.status_code != 200:
        logger.error(f"Failed to fetch news: {response.status_code}", response.text)
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch news")

    return response.json()
