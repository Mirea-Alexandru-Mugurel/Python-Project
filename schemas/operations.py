from pydantic import BaseModel
from datetime import datetime


class OperationRequest(BaseModel):
    number: int


class PowRequest(BaseModel):
    number: int
    exponent: int


class OperationResponse(BaseModel):
    result: int


class RequestLogOut(BaseModel):
    id: int
    operation: str
    input_data: str
    result: int
    timestamp: datetime

    class Config:
        from_attributes = True
