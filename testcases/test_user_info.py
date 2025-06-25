def test_get_user_info(session, base_url, login_token):
    """
    使用登录获取的 token 访问用户信息接口
    """
    url = f"{base_url}/users/2"

    # 设置认证头
    session.headers.update({
        "Authorization": f"Bearer {login_token}"
    })

    response = session.get(url)

    assert response.status_code == 200
    json_data = response.json()
    assert json_data["data"]["id"] == 2
    assert json_data["data"]["email"] == "janet.weaver@reqres.in"