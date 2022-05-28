from fastapi import APIRouter
from app.schemas.v1 import iban
router = APIRouter()


@router.post(
    "/validate",
    response_model=iban.IBANValidateResponse
)
def validate_iban_number(request: iban.IBANValidateRequest):
    return {"message": request.iban}
