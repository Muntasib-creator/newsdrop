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

class Articles(BaseModel):
    articles: list[NewsArticle]
    total: int

class Response(BaseModel):
    data: Optional[Articles] = None
    error: Optional[str] = None
