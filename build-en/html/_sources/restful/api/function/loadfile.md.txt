# Load File

Loads data files. See supported file formats at [Import and Export of Files](../../file_data.md).

## Request description

- Method: `POST`
- URL: `/loadfile`
- Headers:
    - `Content-Type: application/json`
- Body:

    ```json
    {
        "tables": [
            {
                "name": "table_name",
                "format": "csv",
                "path": "/path/to/data.csv",
                "options": {
                    "header": "True",
                    "delimiter": ","
                },
                "schema": [
                    {"column0": "string"},
                    {"column1": "double"},
                    {"column2": "int"}
                ]
            }
        ]
    }
    ```

    Parameter description:

    - `tables`: Creates description of the data table. This field is a list, and the system will build the table in the order indicated by the list.
        - `name`: Name of the data table.
        - `format`: Format of the file to load.
        - `path`: Path to the file.
        - `options`: Options when loading the file, provided as `key-value`.
        - `schema`: Name and type description of each column of data. The `schema` field is a list and its order needs to be consistent with the actual storage order of the columns in the file.

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

url = "http://localhost:8080/loadfile"

# An example of the content of a file at /path/to/data.csv:
"""
column0, column1, column2
str1, 0.1, 1
str2, 0.2, 2
str3, 0.3, 3
"""
payload = {
    "tables": [
        {
            "name": "table_name",
            "format": "csv",
            "path": "/path/to/data.csv",
            "options": {
                "header": "True",
                "delimiter": ","
            },
            "schema": [
                {
                    "column0": "string"
                },
                {
                    "column1": "double"
                },
                {
                    "column2": "int"
                }
            ]
        }
    ]
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
```

### curl

```bash
curl --location --request POST 'http://localhost:8080/loadfile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "tables": [
        {
            "name": "table_name",
            "format": "csv",
            "path": "/path/to/data.csv",
            "options": {
                "header": "True",
                "delimiter": ","
            },
            "schema": [
                {
                    "column0": "string"
                },
                {
                    "column1": "double"
                },
                {
                    "column2": "int"
                }
            ]
        }
    ]
}'
```

## Response example

```json
{
    "status": "success",
    "code": "200",
    "message": "create table successfully!"
}
```
