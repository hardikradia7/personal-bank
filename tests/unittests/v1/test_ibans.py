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


def test_invalid_length_sweden_iban():
    iban = "SE72800008103400097832"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR


def test_illegal_char_sweden_iban():
    iban = "SE72800008103400097832@0"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR


def test_invalid_country_code_iban():
    iban = "IB72800008103400097832@0"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR


def test_valid_albania_iban():
    iban = "AL47212110090000000235698741"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_andorra_iban():
    iban = "AD1200012030200359100100"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_austria_iban():
    iban = "AT611904300234573201"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_azerbaijan_iban():
    iban = "AZ21NABZ00000000137010001944"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_bahrain_iban():
    iban = "BH67BMAG00001299123456"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_belgium_iban():
    iban = "BE68539007547034"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_bosnia_and_herzegovina_iban():
    iban = "BA391290079401028494"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_brazil_iban():
    iban = "BR1800360305000010009795493C1"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_bulgaria_iban():
    iban = "BG80BNBG96611020345678"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_costa_rica_iban():
    iban = "CR05015202001026284066"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_croatia_iban():
    iban = "HR1210010051863000160"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_cyprus_iban():
    iban = "CY17002001280000001200527600"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_czech_republic_iban():
    iban = "CZ6508000000192000145399"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_denmark_iban():
    iban = "DK5000400440116243"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_the_dominican_republic_iban():
    iban = "DO28BAGR00000001212453611324"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_egypt_iban():
    iban = "EG380019000500000000263180002"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_el_salvador_iban():
    iban = "SV62CENR00000000000000700025"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_estonia_iban():
    iban = "EE382200221020145685"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_faroe_islands_iban():
    iban = "FO6264600001631634"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_finland_iban():
    iban = "FI2112345600000785"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_france_iban():
    iban = "FR1420041010050500013M02606"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_georgia_iban():
    iban = "GE29NB0000000101904917"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_germany_iban():
    iban = "DE89370400440532013000"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_gibraltar_iban():
    iban = "GI75NWBK000000007099453"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_greece_iban():
    iban = "GR1601101250000000012300695"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_green_land_iban():
    iban = "GL8964710001000206"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_guatemala_iban():
    iban = "GT82TRAJ01020000001210029690"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_hungary_iban():
    iban = "HU42117730161111101800000000"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_iceland_iban():
    iban = "IS140159260076545510730339"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_ireland_iban():
    iban = "IE29AIBK93115212345678"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_israel_iban():
    iban = "IL620108000000099999999"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_italy_iban():
    iban = "IT60X0542811101000000123456"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_jordan_iban():
    iban = "JO94CBJO0010000000000131000302"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_kazakhstan_iban():
    iban = "KZ86125KZT5004100100"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_kosovo_iban():
    iban = "XK051212012345678906"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_kuwait_iban():
    iban = "KW81CBKU0000000000001234560101"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_latvia_iban():
    iban = "LV80BANK0000435195001"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_lebanon_iban():
    iban = "LB62099900000001001901229114"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_liechtenstein_iban():
    iban = "LI21088100002324013AA"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_lithuania_iban():
    iban = "LT121000011101001000"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_luxembourg_iban():
    iban = "LU280019400644750000"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_macedonia_iban():
    iban = "MK07250120000058984"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_malta_iban():
    iban = "MT84MALT011000012345MTLCAST001S"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_mauritania_iban():
    iban = "MR1300020001010000123456753"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_monaco_iban():
    iban = "MC5811222000010123456789030"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_montenegro_iban():
    iban = "ME25505000012345678951"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_netherlands_iban():
    iban = "NL91ABNA0417164300"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_norway_iban():
    iban = "NO9386011117947"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_pakistan_iban():
    iban = "PK36SCBL0000001123456702"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_palestine_iban():
    iban = "PS92PALS000000000400123456702"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_poland_iban():
    iban = "PL61109010140000071219812874"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_portugal_iban():
    iban = "PT50000201231234567890154"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_qatar_iban():
    iban = "QA58DOHB00001234567890ABCDEFG"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_romania_iban():
    iban = "RO49AAAA1B31007593840000"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_san_marino_iban():
    iban = "SM86U0322509800000000270100"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_saudi_arabia_iban():
    iban = "SA0380000000608010167519"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_serbia_iban():
    iban = "RS35260005601001611379"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_slovakia_iban():
    iban = "SK3112000000198742637541"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_slovenia_iban():
    iban = "SI56263300012039086"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_spain_iban():
    iban = "ES9121000418450200051332"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_switzerland_iban():
    iban = "CH9300762011623852957"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_turkey_iban():
    iban = "TR330006100519786457841326"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_ukraine_iban():
    iban = "UA213223130000026007233566001"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_uae_iban():
    iban = "AE070331234567890123456"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_uk_iban():
    iban = "GB29NWBK60161331926819"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_vatican_city_iban():
    iban = "VA59001123000012345678"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_valid_virgin_islands_iban():
    iban = "VG96VPVG0000012345678901"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_SYNC_SUCCESS


def test_invalid_italy_iban():
    iban = "IT60X0542811101000000123455"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR


def test_invalid_length_italy_iban():
    iban = "IT60X05428111010000001234567"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR


def test_illegal_char_italy_iban():
    iban = "IT60X0542811101#00000123456"
    with TestClient(app) as test_client:
        response = test_client.post(
            IBANS_URI + "/" + "validate",
            json=test_constants.get_iban_validate_request_body(iban)
        )
        assert response.status_code == \
               test_constants.RESPONSE_CODE_BAD_REQUEST_ERROR
