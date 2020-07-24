# Table Schema

Fetches the name and data type of each column in a data table.

## Request description

- Method: `GET`
- URL: `/table/schema?table=table_name`
- table: Name of the table.

## Request example

### Python

Examples in this article use Python's `requests` library. Run the following command to install `requests`:

```bash
pip install requests
```

Sample code:

```python
import requests

url = "http://localhost:8080/table/schema?table=table_name"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text.encode('utf8'))
```

### curl

```bash
curl --location --request GET 'http://localhost:8080/table/schema?table=table_name'
```

## Response example

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
