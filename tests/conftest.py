import os
import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


@pytest.fixture(scope="session")
def api():
    session = requests.Session()

    api_key = os.getenv("REQRES_API_KEY")
    if api_key:
        session.headers["x-api-key"] = api_key

    retry = Retry(
        total=5,
        backoff_factor=2,
        status_forcelist=[429, 502, 503],
        allowed_methods=None,          # retry aussi POST/PUT/DELETE
        respect_retry_after_header=True,
        raise_on_status=False,         # renvoie la réponse au lieu de lever RetryError
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    return session