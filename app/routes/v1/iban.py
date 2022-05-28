import re
from fastapi import APIRouter
from starlette.responses import JSONResponse
from http import HTTPStatus

from app.schemas.v1 import iban
from app.utils import consts
from app.utils import exceptions
from app.utils import error_codes

router = APIRouter()


@router.post(
    "/validate",
    response_model=iban.IBANValidateResponse
)
def validate_iban_number(request: iban.IBANValidateRequest):
    """
    Validate the given IBAN number is valid or not.
    :param request: IBAN number
    :return:
    """
    try:
        iban_str = request.iban.upper().replace(" ", "")

        n = len(iban_str)
        country_code = iban_str[:2]

        # Checking if iban number in input contains any special chars
        if re.search(r'[^a-zA-Z0-9]', iban_str):
            raise exceptions.IllegalIBANCharacter(
                getattr(error_codes, "ILLEGAL_IBAN_CHARACTER")
            )

        # Checking if len of iban number is valid acc to country code
        if n != consts.COUNTRY_CODE_IBAN_LENGTH.get(country_code, 0) or n == 0:
            raise exceptions.InvalidIBANLength(
                getattr(error_codes, "INVALID_IBAN_LENGTH")
            )

        # Rearranging and converting alphabets to int eq and finding modulus of 97
        iban_str = iban_str[4:] + iban_str[:4]
        new_iban_str = ""
        for individual_char in iban_str:
            new_iban_str += consts.CHAR_TO_INT_VALUE.get(individual_char, individual_char)
        new_iban_int = int(new_iban_str)
        if new_iban_int % 97 == 1:
            return {"message": "The IBAN number you provided is valid"}
        else:
            raise exceptions.InvalidIBAN(
                getattr(error_codes, "INVALID_IBAN")
            )

    except exceptions.IBANApiException as ex:
        return JSONResponse(
            content=ex.get_error_dict(),
            status_code=ex.get_error_status_code()
        )
    except Exception as ex:
        return JSONResponse(
            content=getattr(error_codes, "INTERNAL_SERVER_ERROR"),
            status_code=HTTPStatus.INTERNAL_SERVER_ERROR
        )
