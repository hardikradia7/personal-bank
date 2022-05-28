from pydantic import (BaseModel, Field)


class IBANValidateRequest(BaseModel):
    iban: str


class IBANValidateResponse(BaseModel):
    message: str = Field(None, max_length=255)
