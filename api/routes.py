from fastapi import APIRouter, Depends, Query
from typing import List
from schemas.operations import (
    OperationRequest,
    PowRequest,
    OperationResponse,
    RequestLogOut,
)
from services.math_ops import compute_fib, compute_fact, compute_pow
from services.logger import get_last_logs
from auth.api_key import get_api_key

router = APIRouter(prefix="/math", tags=["math"])


@router.post("/fib", response_model=OperationResponse)
async def fib_route(request: OperationRequest, api_key: str = Depends(get_api_key)):
    result = await compute_fib(request)
    return OperationResponse(result=result)


@router.post("/fact", response_model=OperationResponse)
async def fact_route(request: OperationRequest, api_key: str = Depends(get_api_key)):
    result = await compute_fact(request)
    return OperationResponse(result=result)


@router.post("/pow", response_model=OperationResponse)
async def pow_route(request: PowRequest, api_key: str = Depends(get_api_key)):
    result = await compute_pow(request)
    return OperationResponse(result=result)


@router.get("/logs", response_model=List[RequestLogOut])
async def get_logs(
    limit: int = Query(10, ge=1, le=100), api_key: str = Depends(get_api_key)
):
    return await get_last_logs(limit)
