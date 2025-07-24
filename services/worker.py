import asyncio
from models.request_log import RequestLog
from services.logger import logger

log_queue = asyncio.Queue()
shutdown_event = asyncio.Event()


async def worker():
    while not shutdown_event.is_set():
        try:
            task = await asyncio.wait_for(log_queue.get(), timeout=1.0)
        except asyncio.TimeoutError:
            continue

        operation, input_data, result = task
        await RequestLog.create(
            operation=operation, input_data=input_data, result=result
        )
        logger.info(f"[WORKER-LOG] {operation.upper()}({input_data}) = {result} saved")
        log_queue.task_done()


async def enqueue_log_task(operation: str, data: str, result: int):
    await log_queue.put((operation, data, result))


async def start_worker():
    return asyncio.create_task(worker())


async def stop_worker(task):
    shutdown_event.set()
    await task
