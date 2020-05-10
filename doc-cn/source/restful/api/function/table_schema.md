# 获取表的列信息

获取数据表各列的名称与数据类型信息。

## 请求说明

- HTTP方法: **GET**
- 请求URL: /table/schema?scope=scope1&session=spark&table=table1

- scope：该字段指明在哪一个作用域内查询表的信息；
- session：可选参数，该字段指明使用哪个 `SparkSession` 查询表的信息；
- table：表名。

## 样例

### python

本文示例代码使用 python 的 `requests` 库调用 `Arctern Restful API`，使用下面的命令安装 `requests`：

```shell
pip install requests
```

调用示例

```python
import requests

url = "http://localhost:8080/table/schema?scope=scope1&session=spark&table=table1"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
```

### curl

```shell
curl --location --request GET 'http://localhost:8080/table/schema?scope=scope1&session=spark&table=table1'
```

## 返回说明

成功样例：

```json
{
    "table": "table_name",
    "schema": [
        {"column0": "string"},
        {"column1": "double"},
        {"column2": "int"}
    ],
    "num_rows": 500
}
```

失败样例：

```json
{
    "status": "error",
    "code": "-1",
    "message": "table not found!"
}
```

