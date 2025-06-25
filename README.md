# 🔍 API 自动化测试项目 | Pytest + Requests + Reqres API

这是一个基于 Python 的 API 自动化测试项目，使用 `pytest` 框架和 `requests` 库进行接口验证，目标站点为公开测试平台 [reqres.in](https://reqres.in)。项目从 0 搭建，适合初学者练习 API 测试、测试工程师简历作品集展示，也适合作为后续接入 CI/CD 的测试工程。

---

## 🚀 技术栈 & 项目亮点

| 技术 | 用途 |
|------|------|
| ✅ Python 3.10+ | 主语言 |
| ✅ requests | HTTP 请求发送 |
| ✅ pytest | 测试框架、参数化、断言等 |
| ✅ pytest.ini | 测试目录配置与收敛控制 |
| ✅ Session 会话封装 | 保持 header，如统一管理 API Key |
| ✅ 多环境支持 | 使用 conftest 进行统一配置管理 |
| ✅ Git / GitHub | 项目版本管理与协作 |

---

## 📂 项目结构概览

```bash
api-test-framework/
├── testcases/                # 测试用例目录
│   ├── test_login.py         # 登录接口测试
│   └── test_user_info.py     # 用户信息接口测试
│
├── data/                     # 测试数据（json/yaml 等）
│   └── login_data.json       # 登录参数示例
│
├── utils/                    # 工具模块
│   └── request_tool.py       # requests.Session 封装类
│
├── config/                   # 配置目录
│   └── settings.py           # base_url、api-key 等配置
│
├── conftest.py               # Pytest 全局 fixture（如 session）
├── requirements.txt          # 所有依赖包
├── pytest.ini                # pytest 启动配置
└── README.md                 # 项目说明文档
```

---

## 📘 示例用例：登录接口

```python
def test_login_success(session, base_url):
    url = f"{base_url}/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    response = session.post(url, json=payload)
    assert response.status_code == 200
    assert "token" in response.json()
```

---

## ✅ 已完成的接口用例清单

| 模块       | 接口                             | 场景说明                           |
|------------|----------------------------------|------------------------------------|
| 登录接口   | `POST /login`                    | 正常登录、账号/密码为空、错误信息校验 |
| 用户信息   | `GET /users/{id}`                | 校验用户信息返回字段、状态码        |

---

## 📦 快速开始使用

### 安装依赖

```bash
pip install -r requirements.txt
```

### 运行测试

```bash
pytest -v
```

或运行某个指定模块：

```bash
pytest testcases/test_login.py -v
```

---

## 🔐 环境与认证说明

- 本项目使用 `reqres-free-v1` 的 **x-api-key** 验证方式。
- 所有请求通过封装后的 Session 自动添加认证头：

```python
self.session.headers.update({
    "x-api-key": settings.API_KEY
})
```

---

## 🌱 可拓展建议

- ✅ 接入 CI（GitHub Actions / Jenkins）
- ✅ 支持 Allure 报告输出
- ✅ 增加错误日志输出与日志回溯
- ✅ 多接口依赖串联测试
- ✅ 从 YAML / CSV 加载测试数据
- ✅ 支持 token 登录后提取动态 token 自动带入后续请求

---

## 🧑‍💻 作者信息

- **作者**：叶树潭（Shutan Ye）  
- **城市**：深圳  
- **GitHub**：[Tsy-iii](https://github.com/Tsy-iii)

---

## 📌 项目声明

本项目仅用于学习与简历作品展示，测试接口来源于 [reqres.in](https://reqres.in)，该站点为公开模拟接口平台，适合接口测试入门使用，无任何商业用途。