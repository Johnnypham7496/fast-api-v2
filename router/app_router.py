from fastapi import APIRouter, Response, status



router = APIRouter()


@router.get("/", tags=['Welcome'], response_description='Displays welcome message')
async def welcome(repsonse: Response):
    repsonse.status_code = status.HTTP_200_OK
    return {"message": "Hello, welcome to Justice Leagues FastAPI"}


@router.get("/health", tags=['health'], response_description='Returns the health status of this app')
async def health(response: Response):
    response.status_code = status.HTTP_200_OK
    return {"status": "OK"}