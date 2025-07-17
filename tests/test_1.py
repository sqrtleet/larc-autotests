import json
import pytest
from loguru import logger

from core.config import settings


@pytest.mark.api
def test_case_create_application(auth_headers, api_client):
    headers = auth_headers('elma')
    client = api_client(settings.lras_url, headers)
    response = client.get('/api/Enrichment?id=8c38c22c-482d-4c84-90e5-eabd7aac22d3')
    assert response.status_code == 200
