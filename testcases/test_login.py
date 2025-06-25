import pytest
import json
from pathlib import Path

def test_login_success(session, base_url):
    """
    测试成功登录，返回 token
    """
    url = f"{base_url}/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = session.post(url, json=payload)

    assert response.status_code == 200
    assert "token" in response.json()
    
@pytest.mark.parametrize("email, password, expected_error", [
    ("", "cityslicka", "Missing email or username"),
    ("eve.holt@reqres.in", "", "Missing password"),
    ("invalid@email.com", "wrongpass", "user not found"),
])
def test_login_fail(session, base_url, email, password, expected_error):
    """
    登录失败的场景，验证返回的错误信息
    """
    url = f"{base_url}/login"
    payload = {
        "email": email,
        "password": password
    }

    response = session.post(url, json=payload)

    assert response.status_code != 200
    assert expected_error in response.text
    
# 数据驱动测试（读取 json 文件） 的进阶写法
def load_login_test_data():
    data_path = Path(__file__).parent.parent / "data" / "login_data.json"
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)

@pytest.mark.parametrize("case", load_login_test_data())
def test_login_cases(session, base_url, case):
    url = f"{base_url}/login"
    payload = {
        "email": case["email"],
        "password": case["password"]
    }

    response = session.post(url, json=payload)

    assert response.status_code == case["expected_status"]