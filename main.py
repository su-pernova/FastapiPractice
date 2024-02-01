from fastapi import FastAPI

# FastAPI 앱 가동
app = FastAPI()

# 누군가 http://127.0.0.1:8000/equipment 라는 url 로
# GET 이라는 HTTP 요청을 보내면
# {'type': 'Equipment-A', 'name': 'EQ-AAA', 'voltage': 200}
# 라는 데이터를 반환하는 API 를 생성한 것이다.

@app.get("/equipment")
def equipment():
    return {
        'type': 'Equipment-A',
        'name': 'EQ-AAA',
        'voltage': 200
    }

# 앱 실행 명령어
    # uvicorn main:app --reload
    # uvicorn main:app --reload --port=5000 식으로 실행하면 5000 번 포트에서 서버가 실행된다
        # 그러면 http://127.0.0.1:5000/equipment 로도 요청을 보낼 수 있음
        # 서버가 여러개 동시에 필요하면 이렇게 포트를 지정해서 사용하면 됨