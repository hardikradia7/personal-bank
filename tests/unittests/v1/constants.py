RESPONSE_CODE_SYNC_SUCCESS = 200
RESPONSE_CODE_BAD_REQUEST_ERROR = 400


def get_iban_validate_request_body(iban):
    return {
        "iban": iban
    }


