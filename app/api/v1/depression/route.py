from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest
from .schema import DepressionUpdate


router = APIRouter()

@router.post('/depression', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return get_depression()

@router.get('/health', tags=['Depression'])
def info():
    return {"message": "Service is up and running"}

@router.put('/depression', tags=['Depression'])
def update_depression(data: DepressionUpdate):
    return {"message": f"Depression record with ID {data.id} has been updated"}