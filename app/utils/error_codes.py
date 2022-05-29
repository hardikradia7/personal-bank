from app.utils import messages

INTERNAL_SERVER_ERROR = {
    'error_code': '10000',
    'error_message': messages.INTERNAL_SERVER_ERROR_MSG
}

ILLEGAL_IBAN_CHARACTER = {
    'error_code': '10001',
    'error_message': messages.ILLEGAL_IBAN_CHARACTER_MSG
}

INVALID_IBAN_LENGTH = {
    'error_code': '10002',
    'error_message': messages.INVALID_IBAN_LENGTH_MSG
}

INVALID_IBAN = {
    'error_code': '10003',
    'error_message': messages.INVALID_IBAN_MSG
}

COUNTRY_CODE_NOT_SUPPORTED = {
    'error_code': '10004',
    'error_message': messages.COUNTRY_CODE_NOT_SUPPORTED_MSG
}
