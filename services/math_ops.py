from schemas.operations import OperationRequest, PowRequest
from cache.in_memory import cached_fib, cached_fact, cached_pow
from services.logger import logger
from services.worker import enqueue_log_task


async def compute_fib(request: OperationRequest) -> int:
    result = cached_fib(request.number)
    await enqueue_log_task("fib", str(request.number), result)
    logger.info(f"[INLINE] FIB({request.number}) = {result}")
    return result


async def compute_fact(request: OperationRequest) -> int:
    result = cached_fact(request.number)
    await enqueue_log_task("fact", str(request.number), result)
    logger.info(f"[INLINE] FACT({request.number}) = {result}")
    return result


async def compute_pow(request: PowRequest) -> int:
    result = cached_pow(request.number, request.exponent)
    await enqueue_log_task("pow", f"{request.number},{request.exponent}", result)
    logger.info(f"[INLINE] POW({request.number}^{request.exponent}) = {result}")
    return result
