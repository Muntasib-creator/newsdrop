# News Drop

A FastAPI-based backend that anchors top headlines from around the world.

## Features

- Integration with NewsAPI
<!-- - OAuth2 Client Credentials authentication -->
- Save top news to a database
- Filter headlines by country and source
- Unit testing with pytest (80%+ coverage)
- Dockerized setup for easy deployment
- Clean, modular, and production-ready codebase

---

## Setup Instructions

### Prerequisites

- Docker and Docker Compose
- A valid NewsAPI API key (get one at [newsapi.org](https://newsapi.org/register))

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
NEWS_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

### Running with Docker

1. Clone the repository:
```bash
git clone https://github.com/Muntasib-creator/newsdrop.git
cd newsdrop
```

2. Create the `.env` file with your configuration (as shown above)

3. Build and start the containers:
```bash
docker-compose up -d
```

4. The application will be available at:
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### API Endpoints

#### 1. Get All News with Pagination
```http
GET /news
```

**Query Parameters:**
- `page` (integer, optional): Page number (default: 1, min: 1)
- `page_size` (integer, optional): Number of items per page (default: 10, min: 1, max: 100)

**Response:**
```json
{
  "data": {
    "articles": [
      {
        "source": {
          "id": "cnn",
          "name": "CNN"
        },
        "author": "John Doe",
        "title": "Breaking News",
        "description": "Latest updates",
        "url": "https://example.com/news",
        "url_to_image": "https://example.com/image.jpg",
        "published_at": "2024-03-20T10:00:00Z",
        "content": "Full article content..."
      }
    ],
    "total": 100
  },
  "error": ""
}
```

#### 2. Save Latest News
```http
POST /news/save-latest
```

**Description:** Saves the latest 3 news articles to the database.

**Response:**
```json
[
  {
    "source": {
      "id": "bbc-news",
      "name": "BBC News"
    },
    "author": "Jane Smith",
    "title": "Top Story",
    "description": "Important update",
    "url": "https://example.com/top-story",
    "url_to_image": "https://example.com/top-image.jpg",
    "published_at": "2024-03-20T09:00:00Z",
    "content": "Latest breaking news..."
  }
]
```

#### 3. Get Headlines by Country
```http
GET /news/headlines/country/{country_code}
```

**Path Parameters:**
- `country_code` (string): Two-letter ISO 3166-1 country code (e.g., "us", "gb", "in")

**Response:**
```json
{
  "data": {
    "articles": [
      {
        "source": {
          "id": "cnn",
          "name": "CNN"
        },
        "author": "CNN Staff",
        "title": "US News Headline",
        "description": "Latest US news",
        "url": "https://cnn.com/us-news",
        "url_to_image": "https://cnn.com/image.jpg",
        "published_at": "2024-03-20T08:00:00Z",
        "content": "US news content..."
      }
    ],
    "total": 20
  },
  "error": ""
}
```

#### 4. Get Headlines by Source
```http
GET /news/headlines/source/{source_id}
```

**Path Parameters:**
- `source_id` (string): News source identifier (e.g., "bbc-news", "cnn", "reuters")

**Response:**
```json
{
  "data": {
    "articles": [
      {
        "source": {
          "id": "bbc-news",
          "name": "BBC News"
        },
        "author": "BBC Reporter",
        "title": "BBC News Headline",
        "description": "Latest from BBC",
        "url": "https://bbc.com/news",
        "url_to_image": "https://bbc.com/image.jpg",
        "published_at": "2024-03-20T07:00:00Z",
        "content": "BBC news content..."
      }
    ],
    "total": 15
  },
  "error": ""
}
```

#### 5. Filter Headlines
```http
GET /news/headlines/filter
```

**Query Parameters:**
- `country` (string, required): Two-letter ISO 3166-1 country code
- `source` (string, required): News source identifier

**Response:**
```json
{
  "data": {
    "articles": [
      {
        "source": {
          "id": "cnn",
          "name": "CNN"
        },
        "author": "CNN Staff",
        "title": "Filtered News",
        "description": "Filtered news content",
        "url": "https://cnn.com/filtered",
        "url_to_image": "https://cnn.com/filtered-image.jpg",
        "published_at": "2024-03-20T06:00:00Z",
        "content": "Filtered news content..."
      }
    ],
    "total": 10
  },
  "error": ""
}
```

### Testing

To run tests:
```bash
docker-compose exec backend pytest
```


