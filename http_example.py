import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.json())

data = {
    "title": "New task",
    "completed": "True",
    "user_id": 1
}

response_post = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response_post.status_code)
print(response_post.json())

#url encoded

data2 = {"username":"test_one","password":"12345"}
response = httpx.post("https://httpbin.org/post", data=data2)

print(response_post.status_code)
print(response_post.json())

headers = {"Authorization": "Bearer my_secret_token"}

response = httpx.get("https://httpbin.org/get", headers=headers)

print(response.json())  # Заголовки включены в ответ


params = {"userId": 1}

response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)

print(response.url)    # https://jsonplaceholder.typicode.com/todos?userId=1
print(response.json()) # Фильтрованный список задач


files = {"file": {"example.txt", open("example.txt", "rb")}}

response = httpx.post("https://httpbin.org/post", files=files)

print(response.json())  # Ответ с данными о загруженном файле) 