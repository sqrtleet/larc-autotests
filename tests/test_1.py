import json
import pytest
from loguru import logger

from core.config import settings
from utils.tools import to_query_params

CASES = [
    pytest.param(
        {
            "CurrentStatus": 0,
            "ClientAbsId": 237695,
            "Application": {
                "Date": "2025-09-18T04:34:59.766Z",
                "Product": 571,
                "Amount": 50000,
                "HasInsurance": False,
                "HasAdditionalClient": False,
                "IsIncludingAmountForNeeds": False,
                "HasCollateral": False
            }
        },
        {"representativeStatus": 1, "comment": 5},
        id="status=2→comment=1"
    ),
    pytest.param(
        {
            "CurrentStatus": 2,
            "ClientAbsId": 237695,
            "Application": {
                "Date": "2025-09-18T04:34:59.766Z",
                "Product": 571,
                "Amount": 50000,
                "HasInsurance": False,
                "HasAdditionalClient": False,
                "IsIncludingAmountForNeeds": False,
                "HasCollateral": False
            }
        },
        {"representativeStatus": 2, "comment": 1},
        id="status=2→comment=1"
    ),
    pytest.param(
        {
            "CurrentStatus": 2,
            "ClientAbsId": 237695,
            "Application": {
                "Date": "2025-09-18T04:34:59.766Z",
                "Product": 571,
                "Amount": 60000,
                "HasInsurance": False,
                "HasAdditionalClient": False,
                "IsIncludingAmountForNeeds": False,
                "HasCollateral": False
            }
        },
        {"representativeStatus": 2, "comment": 1},
        id="status=2→comment=1"
    ),
]


@pytest.mark.api
def test_case_create_application(auth_headers, api_client):
    headers = auth_headers('elma')
    client = api_client(settings.lras_url, headers)
    params = to_query_params()
    response = client.get('/api/AuthorizedPerson/GetRepresentivePersonStatus')
    assert response.status_code == 200
