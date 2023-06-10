import uvicorn

from fastapi import FastAPI, Response, status

app = FastAPI()


@app.get("/", tags=['Welcome'], response_description='Displays welcome message')
async def welcome(repsonse: Response):
    repsonse.status_code = status.HTTP_200_OK
    return {"message": "Hello, welcome to Justice Leagues FastAPI"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)