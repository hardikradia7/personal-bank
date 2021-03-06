from http import HTTPStatus
from app.utils import error_codes


class IBANApiException(Exception):
    error_status_code = HTTPStatus.INTERNAL_SERVER_ERROR

    def __init__(self, error=error_codes.INTERNAL_SERVER_ERROR):
        if error:
            self.error_code = error.get("error_code")
            self.error_message = error.get("error_message")
            self.error_status_code = error.get('error_status_code')

    def get_error_dict(self):
        return {
            'code': self.error_code,
            'message': self.error_message
        }

    def get_error_code(self):
        return self.error_code

    def get_error_message(self):
        return self.error_message

    def get_error_status_code(self):
        return self.error_status_code


class IllegalIBANCharacter(IBANApiException):
    def __init__(self, error=None):
        error['error_status_code'] = HTTPStatus.BAD_REQUEST
        super(). __init__(error)


class CountryCodeNotSupported(IBANApiException):
    def __init__(self, error=None):
        error['error_status_code'] = HTTPStatus.BAD_REQUEST
        super(). __init__(error)


class InvalidIBANLength(IBANApiException):
    def __init__(self, error=None):
        error['error_status_code'] = HTTPStatus.BAD_REQUEST
        super().__init__(error)


class InvalidIBAN(IBANApiException):
    def __init__(self, error=None):
        error['error_status_code'] = HTTPStatus.BAD_REQUEST
        super().__init__(error)
