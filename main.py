import uvicorn

from fastapi import FastAPI, Response, status

app = FastAPI(
    title="Justice Leagues FastAPI",
    description="This is the swagger page for Justice Leagues FastAPI",
    version='1.0.0'
)


@app.get("/", tags=['Welcome'], response_description='Displays welcome message')
async def welcome(repsonse: Response):
    repsonse.status_code = status.HTTP_200_OK
    return {"message": "Hello, welcome to Justice Leagues FastAPI"}


@app.get("/health", tags=['health'], response_description='Returns the health status of this app')
async def health(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)