# name = "小明"
# age = 20
# print(f"姓名: {name}, 年齡: {age}")

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"msg": "ok"}
    
@app.get("/stock")
def stock():

    return {
        "NVDA": 215.2,
        "AAPL": 293.3
    }
