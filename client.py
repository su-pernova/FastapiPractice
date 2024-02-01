import requests

# 요청을 보낼 url
url = "http://127.0.0.1:8000/equipment"

# 해당 url 에 GET 요청을 보내 데이터를 받아온다
response = requests.get(url=url)

# 받아온 데이터 출력해보기
print("status_code: ", response.status_code)
print("content: ", response.json())