import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    filename="news-api.log",
)

logger = logging.getLogger("news-api")
