import os

import psycopg2
import pytest
import requests
import urllib3
from datetime import datetime
from psycopg2.extras import RealDictCursor

from core.config import settings

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class APIClient:
    def __init__(self, base_url: str, token: dict):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(token)

    def request(self, method: str, path: str, **kwargs):
        url = f'{self.base_url}{path}'
        response = self.session.request(method, url, **kwargs, verify=False)
        response.raise_for_status()
        return response

    def get(self, path: str, **kwargs):
        return self.request('GET', path, **kwargs)

    def post(self, path: str, **kwargs):
        return self.request('POST', path, **kwargs)

    def patch(self, path: str, **kwargs):
        return self.request('PATCH', path, **kwargs)

    def delete(self, path: str, **kwargs):
        return self.request('DELETE', path, **kwargs)


@pytest.fixture(scope='session')
def auth_headers():
    cache = {}

    def _get_token_headers(target: str) -> dict:
        if target not in cache:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            body = settings.auth_body.get(target)
            if body is None:
                raise KeyError(f'Не найдено тело запроса для target="{target}" в settings.auth_body')
            response = requests.post(settings.auth_url, headers=headers, data=body, verify=False)
            response.raise_for_status()
            token = response.json().get('access_token')
            if not token:
                raise ValueError(f'Не удалось получить токен для target="{target}"')
            cache[target] = {'Authorization': f'Bearer {token}'}
        return cache[target]

    return _get_token_headers


@pytest.fixture(scope='session')
def api_client():
    def _get_client(target: str, auth_headers) -> APIClient:
        return APIClient(target, auth_headers)

    return _get_client


@pytest.fixture(scope='session')
def db_connection():
    conn = psycopg2.connect(settings.database_url)
    yield conn
    conn.close()


@pytest.fixture(scope='function')
def db_cursor(db_connection):
    cursor = db_connection.cursor(cursor_factory=RealDictCursor)
    yield cursor
    # db_connection.rollback()
    cursor.close()


@pytest.fixture(scope='session')
def aggregate_id():
    return '3eba5ebf-06d6-423c-995c-25e6409ecf0c'
