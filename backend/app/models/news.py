from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

class Source(BaseModel):
    id: str | None
    name: str

class NewsArticle(BaseModel):
    source: Source
    author: str | None
    title: str | None
    description: str | None
    url: str | None
    url_to_image: str | None
    published_at: str | None
    content: str | None


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
        content="This is a dummy content for the news article."
    ),
    NewsArticle(
        author="Jane Smith",
        title="Global Climate Summit Reaches Historic Agreement",
        description="World leaders have agreed on new measures to combat climate change.",
        url="https://example.com/world-news/1",
        url_to_image="https://example.com/world-news/1",
        published_at=datetime.now().isoformat(),
        source=Source(id="world-news", name="World News"),
        content="This is a dummy content for the news article."
    ),
]

class Articles(BaseModel):
    articles: list[NewsArticle]
    total: int

class Response(BaseModel):
    data: Optional[Articles] = None
    error: Optional[str] = None
