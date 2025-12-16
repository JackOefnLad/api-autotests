import httpx
from tools.fakers import get_random_email

user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_response = httpx.post("http://localhost:8000/api/v1/users", json=user_payload)

print(create_response.status_code)
print(create_response.json())