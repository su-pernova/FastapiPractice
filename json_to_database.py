import requests
import pymysql
import json

# - - - - - - - - client - - - - - - - -
url = "http://127.0.0.1:8000/equipment"

# 해당 url 에 GET 요청을 보내 데이터를 받아온다
response = requests.get(url=url)
json_data = response.json()


# - - - - - - - database - - - - - - -
database = pymysql.connect(
    host = "localhost",
    port=3306,
    user = "root",
    password = "1234",
    database = "test_schema",
	charset = 'utf8'
)

# cursor object 가져오기
cursor = database.cursor()

# 위에서 받아온 json_data 데이터에서 값을 추출한다.
type = json_data['type']
name = json_data['name']
voltage = json_data['voltage']

# 데이터베이스에 값 저장
sql = "INSERT INTO equipment(type, name, voltage) VALUES (%s, %s, %s)"
val = (type, name, int(voltage))

cursor.execute(sql, val)
database.commit()

# 작업이 완료되면 아래 문구 출력
print(cursor.rowcount, "record inserted")