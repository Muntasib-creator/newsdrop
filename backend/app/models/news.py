from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field

class NewsArticle(BaseModel):
    title: str
    description: str
    url: str
    published_at: datetime
    source_id: str
    country_code: str

# Dummy data
DUMMY_NEWS = [
    NewsArticle(
        title="Tech Giant Announces Revolutionary AI Breakthrough",
        description="A major tech company has unveiled its latest AI innovation that promises to transform the industry.",
        url="https://example.com/tech-news/1",
        published_at=datetime.now(),
        source_id="tech-news",
        country_code="us"
    ),
    NewsArticle(
        title="Global Climate Summit Reaches Historic Agreement",
        description="World leaders have agreed on new measures to combat climate change.",
        url="https://example.com/world-news/1",
        published_at=datetime.now(),
        source_id="world-news",
        country_code="gb"
    ),
    NewsArticle(
        title="New Study Reveals Benefits of Mediterranean Diet",
        description="Research confirms the health benefits of traditional Mediterranean eating patterns.",
        url="https://example.com/health-news/1",
        published_at=datetime.now(),
        source_id="health-news",
        country_code="it"
    ),
    NewsArticle(
        title="Stock Markets Reach All-Time High",
        description="Global markets have achieved record levels amid economic recovery.",
        url="https://example.com/business-news/1",
        published_at=datetime.now(),
        source_id="business-news",
        country_code="us"
    ),
    NewsArticle(
        title="Major Sports Event Set to Begin",
        description="The world's largest sporting event is about to commence with record participation.",
        url="https://example.com/sports-news/1",
        published_at=datetime.now(),
        source_id="sports-news",
        country_code="jp"
    )
]

class NewsResponse(BaseModel):
    articles: List[NewsArticle]
    total: int
    page: int
    size: int 