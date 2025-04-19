# News Drop

A FastAPI-based backend that anchors top headlines from around the world.

## Features

- Integration with NewsAPI
- OAuth2 Client Credentials authentication
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
- Python 3.10+ (if running without Docker)

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
NEWS_API_KEY=your_api_key_here
DATABASE_URL=postgresql://user:pass@db:5432/mydb
```

### Running with Docker

1. Clone the repository:
```bash
git clone <repository-url>
cd newsdrop
```

2. Create the `.env` file with your configuration (as shown above)

3. Build and start the containers:
```bash
docker-compose up --build
```

4. The application will be available at:
- Backend API: http://localhost:8000
- API Documentation: http://localhost:8000/docs

### API Endpoints

- `GET /news` - Get all news with pagination
- `POST /news/save-latest` - Save the latest 3 news articles to database
- `GET /news/headlines/country/{country_code}` - Get headlines by country
- `GET /news/headlines/source/{source_id}` - Get headlines by source
- `GET /news/headlines/filter` - Filter headlines by country and source

### Development

To run tests:
```bash
docker-compose exec backend pytest
```
