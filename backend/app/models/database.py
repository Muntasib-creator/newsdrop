from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class NewsArticle(Base):
    __tablename__ = "news_articles"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String(100), nullable=True)
    source_name = Column(String(255), nullable=True)
    author = Column(String(255), nullable=True)
    title = Column(String(500), nullable=True)
    description = Column(Text, nullable=True)
    url = Column(String(500), nullable=True)
    url_to_image = Column(String(500), nullable=True)
    published_at = Column(DateTime, nullable=True)
    content = Column(Text, nullable=True)

    def __repr__(self):
        return f"<NewsArticle {self.title}>" 