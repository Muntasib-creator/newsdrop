from dotenv import load_dotenv
import os

load_dotenv()

class Settings( ):
    news_api_key: str = os.getenv("NEWS_API_KEY")
    database_url: str = os.getenv("DATABASE_URL")

settings = Settings()