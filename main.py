import uvicorn

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)