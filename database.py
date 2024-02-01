import pymysql.cursors

# 데이터베이스 접속 정보 입력
database = pymysql.connect(
    host = "localhost",
    port=3306,
    user = "root",             # MySQL 설치 당시 입력했던 user 값 입력. 설정한 적 없다면 아마 기본 값은 root 일거임
    password = "1234",         # MySQL 설치 당시 입력했던 password 값 입력. 설정한 적 없다면 아마 기본 값이 0000 일거임
    database = "test_schema",  # equipment 테이블을 생성했던 스키마(데이터베이스) 이름 입력
)

# cursor object 가져오기
cursor = database.cursor()

# 데이터베이스에 값 저장
sql = "INSERT INTO equipment(type, name, voltage) VALUES (%s, %s, %s)"
val = ("test_type", "test_name", int(999))

cursor.execute(sql, val)
database.commit()

# 작업이 완료되면 아래 문구 출력
print(cursor.rowcount, "record inserted")