from typing import Optional
from fastapi import APIRouter, Query, HTTPException, Depends
from app.models.news import NewsArticle as NewsArticleModel, Response, Articles
from app.schema.news_articles import NewsArticle
from app.services.newsapi import fetch_news, fetch_headlines
from app.database import get_db
from sqlalchemy.orm import Session
import json

router = APIRouter(prefix="/news", tags=["news"])

@router.get("", response_model=Response)
async def get_news(
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100)
):
    """Get all news with pagination support"""
    news_data = await fetch_news(page=page, pageSize=page_size)
    # print(json.dumps(news_data, indent=4))
    articles = [NewsArticleModel(
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
        ),
        error=""
    )

@router.post("/save-latest", response_model=list[NewsArticleModel])
async def save_latest_news(db: Session = Depends(get_db)):
    """Save the latest 3 news articles to database"""
    news_data = await fetch_news(page=1, pageSize=3)
    saved_articles = NewsArticle.save_latest_articles(db, news_data["articles"])
    return [NewsArticleModel(
        author=article.author,
        title=article.title,
        description=article.description,
        url=article.url,
        url_to_image=article.url_to_image,
        published_at=article.published_at.isoformat(),
        source={"id": article.source_id, "name": article.source_name},
        content=article.content
    ) for article in saved_articles]

@router.get("/headlines/country/{country_code}", response_model=Response)
async def get_headlines_by_country(country_code: str):
    """Get top headlines by country"""
    headlines = await fetch_headlines(country=country_code)
    # print(json.dumps(headlines, indent=4))
    articles = [NewsArticleModel(
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
    # print(json.dumps(headlines, indent=4))
    if 'error' in headlines:
        raise HTTPException(status_code=500, detail=headlines["error"])
    articles = [NewsArticleModel(
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

@router.get("/headlines/filter", response_model=Response)
async def filter_headlines(
    country: str,
    source: str
):
    """Get top headlines filtered by country and source"""
    headlines = await fetch_headlines(country=country)
    # print(json.dumps(headlines, indent=4))
    articles = [NewsArticleModel(
        author=article["author"],
        title=article["title"],
        description=article["description"],
        url=article["url"],
        url_to_image=article["urlToImage"],
        published_at=article["publishedAt"],
        source=article["source"],
        content=article["content"]
    ) for article in headlines["articles"] if article["source"]["id"] and article["source"]["id"].lower() == source.lower()]
    return Response(
        data=Articles(
            articles=articles,
            total=len(articles),
        ),
        error=""
    )