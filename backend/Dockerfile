# Use official Python image
FROM python:3.11-slim

WORKDIR /app

# Install uv
RUN apt-get update && apt-get install -y curl && \
    mkdir -p /usr/local/bin && \
    curl -L https://github.com/astral-sh/uv/releases/latest/download/uv-x86_64-unknown-linux-gnu.tar.gz | tar xzf - -C /usr/local/bin --strip-components=1 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a minimal README.md since pyproject.toml needs it
RUN echo "# NewsAPI Backend" > README.md

# Copy pyproject.toml for dependency installation
COPY pyproject.toml .

# Install dependencies using uv without editable mode
RUN uv pip install --system .

# Copy application code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
