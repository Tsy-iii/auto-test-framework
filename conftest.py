import pytest
import requests
from config import settings

@pytest.fixture(scope="session")
def base_url():
    return settings.BASE_URL

# 把 session 的作用域从默认的 function 改成 session
@pytest.fixture(scope="session")
def session():
    s = requests.Session()
    s.headers.update({
        "Content-Type": "application/json",
        "x-api-key": settings.API_KEY
    })
    return s

# 登录并获取 token
@pytest.fixture(scope="session")
def login_token(base_url, session):
    url = f"{base_url}/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = session.post(url, json=payload)
    token = response.json().get("token")
    assert token is not None, "登录失败，未获取到 token"
    return token