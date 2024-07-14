# CCFtest


1. 导出requirements.txt
```shell
pip freeze > requirements.txt
```
2. 安装requirements.txt
```shell
pip install -r requirements.txt
```
3. 在 Python 的 `requests` 库中，对于 `GET`、`POST`、`PUT` 和 `DELETE` 等请求方法携带请求参数的方式如下：

**GET 请求**：
通常将参数放在 URL 中，使用 `params` 参数。
```python
import requests

url = 'https://example.com/api'
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, params=params)
```

**POST 请求**：
- 如果是表单数据（`application/x-www-form-urlencoded` 格式），使用 `data` 参数。
```python
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, data=data)
```
- 如果是 JSON 数据（`application/json` 格式），使用 `json` 参数。
```python
json_data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post(url, json=json_data)
```

**PUT 请求**：
与 `POST` 请求类似。
- 表单数据使用 `data` 参数。
- JSON 数据使用 `json` 参数。

**DELETE 请求**：
参数通常也放在 URL 中，使用 `params` 参数。
```python
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.delete(url, params=params)
```

例如，假设我们有一个简单的接口，用于获取用户信息（`GET`）、创建用户（`POST`）、更新用户信息（`PUT`）和删除用户（`DELETE`）：

```python
# GET 获取用户信息
get_url = 'https://example.com/users'
get_params = {'user_id': 1}
get_response = requests.get(get_url, params=get_params)

# POST 创建用户
post_url = 'https://example.com/users'
post_data = {'username': 'new_user', 'email': 'new_user@example.com'}
post_response = requests.post(post_url, data=post_data)

# PUT 更新用户信息
put_url = 'https://example.com/users/1'
put_data = {'username': 'updated_user'}
put_response = requests.put(put_url, data=put_data)

# DELETE 删除用户
delete_url = 'https://example.com/users/1'
delete_params = {}
delete_response = requests.delete(delete_url, params=delete_params)
```

请注意，实际使用时应根据接口的具体要求和返回的数据类型来选择合适的参数传递方式。

4. 
```python
import pytest

class TestExample:

    @pytest.mark.parametrize("param1, param2", [
        (1, 'a'),
        (2, 'b'),
        (3, 'c')
    ])
    def test_with_two_parameters(self, param1, param2):
        print(f"Testing with param1: {param1} and param2: {param2}")
        # 在这里添加你的测试逻辑
```
5. @allure.feature('加在类上')|@allure.story('加在方法上')

6. jsonpath解析数据
```python
    r = requests.post(url, json=req_body)
    res = jsonpath.jsonpath(r.json(), '$..Content-Type')
```
