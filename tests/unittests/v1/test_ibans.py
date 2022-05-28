from fastapi.testclient import TestClient

from app.main import app
from app.utils import constants
from tests.unittests.v1 import constants as test_constants

BASE_URI = constants.API + "/" + constants.VERSION_1
IBANS_URI = BASE_URI + "/" + constants.IBANS


def test_valid_sweden_iban():
    iban = "SE7280000810340009783242"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_invalid_sweden_iban():
    iban = "SE7280000810340009783240"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR
