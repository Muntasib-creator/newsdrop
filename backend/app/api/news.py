from typing import Optional
from fastapi import APIRouter, Query, HTTPException
from app.models.news import NewsArticle, NewsResponse, DUMMY_NEWS

router = APIRouter(prefix="/news", tags=["news"])

@router.get("", response_model=NewsResponse)
async def get_news(
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1, le=100)
):
    """Get all news with pagination support"""
    start = (page - 1) * size
    end = start + size
    articles = DUMMY_NEWS[start:end]
    
    return NewsResponse(
        articles=articles,
        total=len(DUMMY_NEWS),
        page=page,
        size=size
    )

@router.post("/save-latest", response_model=list[NewsArticle])
async def save_latest_news():
    """Save the latest 3 news articles"""
    # In a real implementation, this would save to a database
    latest_news = DUMMY_NEWS[:3]
    return latest_news

@router.get("/headlines/country/{country_code}", response_model=list[NewsArticle])
async def get_headlines_by_country(country_code: str):
    """Get top headlines by country"""
    filtered_news = [article for article in DUMMY_NEWS if article.country_code.lower() == country_code.lower()]
    if not filtered_news:
        raise HTTPException(status_code=404, detail=f"No news found for country code: {country_code}")
    return filtered_news

@router.get("/headlines/source/{source_id}", response_model=list[NewsArticle])
async def get_headlines_by_source(source_id: str):
    """Get top headlines by source"""
    filtered_news = [article for article in DUMMY_NEWS if article.source_id.lower() == source_id.lower()]
    if not filtered_news:
        raise HTTPException(status_code=404, detail=f"No news found for source: {source_id}")
    return filtered_news

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