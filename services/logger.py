import logging
import os
from models.request_log import RequestLog

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    format="%(asctime)s | %(levelname)s | %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)


async def get_last_logs(limit: int = 10):
    return await RequestLog.all().order_by("-timestamp").limit(limit)
