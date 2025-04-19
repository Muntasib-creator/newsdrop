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
        try:
            json_response = response.json()
            logger.error(f"Failed to fetch news: {response.status_code}", json_response)
            error_message = json_response.get("message", "Failed to fetch news")
        except:
            logger.error(f"Failed to fetch news: {response.status_code}", response.text)
            error_message = "Failed to fetch news"
        raise HTTPException(status_code=500, error=error_message)

    json_response = response.json()
    if json_response.get("status") == "ok":
        return json_response
    else:
        raise HTTPException(status_code=500, error=json_response.get("message", "Failed to fetch news"))

async def fetch_headlines(country: str = "", source: str = ""):
    logger.info(f"Fetching headlines for country: {country}, source: {source}")
    ENDPOINT = "/top-headlines"
    url = f"{NEWS_API_URL}{ENDPOINT}"
    headers = {
        "X-Api-Key": settings.news_api_key,
    }
    params = dict()
    if country:
        params["country"] = country
    if source:
        params["sources"] = source

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)

    if response.status_code != 200:
        try:
            json_response = response.json()
            logger.error(f"Failed to fetch headlines: {response.status_code}", json_response)
            error_message = json_response.get("message", "Failed to fetch headlines")
        except:
            logger.error(f"Failed to fetch headlines: {response.status_code}", response.text)
            error_message = "Failed to fetch headlines"
        raise HTTPException(status_code=500, error=error_message)

    json_response = response.json()
    if json_response.get("status") == "ok":
        return json_response
    else:
        raise HTTPException(status_code=500, error=json_response.get("message", "Failed to fetch headlines"))

