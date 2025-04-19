from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Source(BaseModel):
    id: str
    name: str

class NewsArticle(BaseModel):
    author: str
    title: str
    description: str
    url: str
    url_to_image: str
    published_at: str
    source: Source

# Dummy data
DUMMY_NEWS = [
    NewsArticle(
        author="John Doe",
        title="Tech Giant Announces Revolutionary AI Breakthrough", 
        description="A major tech company has unveiled its latest AI innovation that promises to transform the industry.",
        url="https://example.com/tech-news/1",
        url_to_image="https://example.com/tech-news/1",
        published_at=datetime.now().isoformat(),
        source=Source(id="tech-news", name="Tech News"),
    ),
    NewsArticle(
        author="Jane Smith",
        title="Global Climate Summit Reaches Historic Agreement",
        description="World leaders have agreed on new measures to combat climate change.",
        url="https://example.com/world-news/1",
        url_to_image="https://example.com/world-news/1",
        published_at=datetime.now().isoformat(),
        source=Source(id="world-news", name="World News"),
    ),
]

class NewsResponse(BaseModel):
    articles: list[NewsArticle]
    total: int
    page: int
    pageSize: int 