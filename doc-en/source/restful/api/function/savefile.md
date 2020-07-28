# Save File

Executes data queries and saves the results to specified files. Only applicable to the PySpark backend. In case of the Python backend, use the `command` interface to save the files. See [interface description for code execution](command.md).

## Request description

- Method: `POST`
- URL: `/savefile`
- Headers:
    - `Content-Type: application/json`
- Body:

    ```json
    {
        "tables": [
            {
                "sql": "select * from table_name",
                "format": "csv",
                "path": "/path/to/data.csv",
                "options": {
                    "header": "True",
                    "delimiter": ","
                }
            }
        ]
    }
    ```

    Parameter description:

    - `tables`: Descriptions when saving data as a file. This field is a list, and the system will save the files in the order indicated by the list.
        - `sql`: The SQL query statement to execute, the result of which is the table to save.
        - `format`: Format of the file to save.
        - `path`: Path to the file.
        - `options`: Options when saving the file, provided as `key-value`.

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

url = "http://localhost:8080/savefile"

payload = {
    "tables": [
        {
            "sql": "select * from table_name",
            "format": "csv",
            "path": "/path/to/data.csv",
            "options": {
                "header": "True",
                "delimiter": ","
            }
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
curl --location --request POST 'http://localhost:8080/savefile' \
--header 'Content-Type: application/json' \
--data-raw '{
    "tables": [
        {
            "sql": "select * from table_name",
            "format": "csv",
            "path": "/path/to/data.csv",
            "options": {
                "header": "True",
                "delimiter": ","
            }
        }
    ]
}'
```

## Response example

```json
{
    "status": "success",
    "code": "200",
    "message": "save table successfully!"
}
```
