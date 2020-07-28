# Code Execution

Executes a given Python code.

## Request description

- Method: `POST`
- URL: `/command`
- Headers:
    - `Content-Type: application/json`
- Body:

    ```json
    {
        "command": "import sys\nprint(len(sys.argv))"
    }
    ```

    Parameter description:

    - `command`: The Python code to execute.

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

url = "http://localhost:8080/command"

payload = {
    "command": "import sys\nprint(len(sys.argv))"
}
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text.encode('utf8'))
```

### curl

```bash
curl --location --request POST 'http://localhost:8080/command' \
--header 'Content-Type: application/json' \
--data-raw '{
	"command":"import sys\nprint(len(sys.argv))"
}'
```

## Response example

```json
{
    "status": "success",
    "code": "200",
    "message": "execute command successfully!"
}
```
