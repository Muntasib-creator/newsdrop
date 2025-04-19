from typing import Optional
from fastapi import APIRouter, Query, HTTPException
from app.models.news import NewsArticle, Response, DUMMY_NEWS, Articles
# from app.settings import settings
from app.services.newsapi import fetch_news, fetch_headlines
import json

router = APIRouter(prefix="/news", tags=["news"])

@router.get("", response_model=Response)
async def get_news(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    """Get all news with pagination support"""
    news_data = await fetch_news(page=page, pageSize=page_size)
    print(json.dumps(news_data, indent=4))
    articles = [NewsArticle(
        author=article["author"],
        title=article["title"],
        description=article["description"],
        url=article["url"],
        url_to_image=article["urlToImage"],
        published_at=article["publishedAt"],
        source=article["source"],
        content=article["content"]
    ) for article in news_data["articles"]]
    return Response(
        data=Articles(
            articles=articles,
            total=news_data["totalResults"],
        )
    )

@router.post("/save-latest", response_model=list[NewsArticle])
async def save_latest_news():
    """Save the latest 3 news articles"""
    # In a real implementation, this would save to a database
    latest_news = DUMMY_NEWS[:3]
    return latest_news

@router.get("/headlines/country/{country_code}", response_model=Response)
async def get_headlines_by_country(country_code: str):
    """Get top headlines by country"""
    headlines = await fetch_headlines(country=country_code)
    print(json.dumps(headlines, indent=4))
    articles = [NewsArticle(
        author=article["author"],
        title=article["title"],
        description=article["description"],
        url=article["url"],
        url_to_image=article["urlToImage"],
        published_at=article["publishedAt"],
        source=article["source"],
        content=article["content"]
    ) for article in headlines["articles"]]
    return Response(
        data=Articles(
            articles=articles,
            total=headlines["totalResults"],
        ),
        error=""
    )

@router.get("/headlines/source/{source_id}", response_model=Response)
async def get_headlines_by_source(source_id: str):
    """Get top headlines by source"""
    headlines = await fetch_headlines(source=source_id)
    print(json.dumps(headlines, indent=4))
    if 'error' in headlines:
        raise HTTPException(status_code=500, detail=headlines["error"])
    articles = [NewsArticle(
        author=article["author"],
        title=article["title"],
        description=article["description"],
        url=article["url"],
        url_to_image=article["urlToImage"],
        published_at=article["publishedAt"],
        source=article["source"],
        content=article["content"]
    ) for article in headlines["articles"]]
    return Response(
        data=Articles(
            articles=articles,
            total=headlines["totalResults"],
        ),
        error=""
    )

@router.get("/headlines/filter", response_model=list[NewsArticle])
async def filter_headlines(
    country: Optional[str] = None,
    source: Optional[str] = None
):
    """Get top headlines filtered by country and/or source"""
    filtered_news = DUMMY_NEWS
    
    if country:
        filtered_news = [article for article in filtered_news if article.country_code.lower() == country.lower()]
    
    if source:
        filtered_news = [article for article in filtered_news if article.source_id.lower() == source.lower()]
    
    if not filtered_news:
        raise HTTPException(status_code=404, detail="No news found matching the criteria")
    
    return filtered_news 