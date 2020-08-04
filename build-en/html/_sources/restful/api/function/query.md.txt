# Query

Executes a given SQL query statement. Only applicable to the PySpark backend.

## Request description

- Method: `POST`
- URL: `/query`
- Headers:
    - `Content-Type: application/json`
- Body:

    - Data query:

    ```json
    {
        "sql": "select * from table_name limit 1",
        "collect_result": "1"
    }
    ```

    - Create a data table:

    ```json
    {
        "sql": "create table new_table as (select * from table_name)",
        "collect_result": "0"
    }
    ```

    Parameter description:

    - `sql`: The SQL query statement to execute.
    - `collect_result`: Optional parameter; default value is "1".
        - 1: Returns the SQL query result in JSON.
        - 0: Runs the query only in backend and doesn't return a result.

## Request example

### Python

Examples in this article use Python's `requests` library. Run the following command to install `requests`:

```bash
pip install requests
```

Sample code:

```python
import requests
import json

url = "http://localhost:8080/query"

payload = {
    "sql": "select * from table_name limit 1",
    "collect_result": "1"
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
```

```python
import requests
import json

url = "http://localhost:8080/query"

payload = {
    "sql": "create table new_table as (select * from table_name)",
    "collect_result": "0"
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
```

### curl

```bash
curl --location --request POST 'http://localhost:8080/query' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sql": "select * from table_name limit 1",
    "collect_result": "1"
}'
```

```bash
curl --location --request POST 'http://localhost:8080/query' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sql": "create table new_table as (select * from table_name)",
    "collect_result": "0"
}'
```

## Response example

```json
{
    "status": "succuss",
    "code": "200",
    "result": [
        ["col1", 0.5, 2]
    ],
    "message": "execute sql successfully!"
}
```
