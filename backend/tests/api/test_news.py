import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
from datetime import datetime
from app.main import app
from app.models.news import NewsArticle, Source

client = TestClient(app)

@pytest.fixture
def mock_news_data():
    return {
        "articles": [
            {
                "author": "Test Author",
                "title": "Test Title",
                "description": "Test Description",
                "url": "https://test.com",
                "urlToImage": "https://test.com/image.jpg",
                "publishedAt": datetime.now().isoformat(),
                "source": {"id": "test-source", "name": "Test Source"},
                "content": "Test Content"
            }
        ],
        "totalResults": 1,
        "status": "ok"
    }

@pytest.fixture
def mock_headlines_data():
    return {
        "articles": [
            {
                "author": "Headline Author",
                "title": "Headline Title",
                "description": "Headline Description",
                "url": "https://headline.com",
                "urlToImage": "https://headline.com/image.jpg",
                "publishedAt": datetime.now().isoformat(),
                "source": {"id": "headline-source", "name": "Headline Source"},
                "content": "Headline Content"
            }
        ],
        "totalResults": 1,
        "status": "ok"
    }

def test_get_news(mock_news_data):
    with patch('app.services.newsapi.fetch_news', return_value=mock_news_data):
        response = client.get("/news?page=1&page_size=10")
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["total"] == 1
        assert len(data["data"]["articles"]) == 1
        assert data["data"]["articles"][0]["title"] == "Test Title"

def test_get_news_invalid_page():
    response = client.get("/news?page=0&page_size=10")
    assert response.status_code == 422

def test_get_news_invalid_page_size():
    response = client.get("/news?page=1&page_size=0")
    assert response.status_code == 422

def test_save_latest_news():
    response = client.post("/news/save-latest")
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_headlines_by_country(mock_headlines_data):
    with patch('app.services.newsapi.fetch_headlines', return_value=mock_headlines_data):
        response = client.get("/news/headlines/country/us")
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["total"] == 1
        assert len(data["data"]["articles"]) == 1
        assert data["data"]["articles"][0]["title"] == "Headline Title"

def test_get_headlines_by_source(mock_headlines_data):
    with patch('app.services.newsapi.fetch_headlines', return_value=mock_headlines_data):
        response = client.get("/news/headlines/source/bbc-news")
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["total"] == 1
        assert len(data["data"]["articles"]) == 1
        assert data["data"]["articles"][0]["title"] == "Headline Title"

def test_get_headlines_by_source_error():
    with patch('app.services.newsapi.fetch_headlines', return_value={"error": "API Error"}):
        response = client.get("/news/headlines/source/invalid-source")
        assert response.status_code == 500

def test_filter_headlines(mock_headlines_data):
    with patch('app.services.newsapi.fetch_headlines', return_value=mock_headlines_data):
        response = client.get("/news/headlines/filter?country=us&source=bbc-news")
        assert response.status_code == 200
        data = response.json()
        assert data["data"]["total"] == 1
        assert len(data["data"]["articles"]) == 1
        assert data["data"]["articles"][0]["title"] == "Headline Title"

def test_filter_headlines_missing_params():
    response = client.get("/news/headlines/filter")
    assert response.status_code == 422 