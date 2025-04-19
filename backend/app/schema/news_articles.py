from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
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

    @classmethod
    def save_latest_articles(cls, db: Session, articles: list[dict]) -> list["NewsArticle"]:
        # Delete all existing articles
        db.query(cls).delete()

        new_articles = []
        for article in articles[:3]:
            news_article = cls(
                source_id=article["source"]["id"],
                source_name=article["source"]["name"],
                author=article["author"],
                title=article["title"],
                description=article["description"],
                url=article["url"],
                url_to_image=article["urlToImage"],
                published_at=datetime.fromisoformat(article["publishedAt"].replace("Z", "+00:00")),
                content=article["content"]
            )
            db.add(news_article)
            new_articles.append(news_article)
        
        db.commit()
        return new_articles 