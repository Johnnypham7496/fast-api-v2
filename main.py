import uvicorn
from sqlalchemy.orm import Session
from fastapi import FastAPI, Response, status, Depends
from db_config import engine, get_db
from repository import users_repository
from db import user_db

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


@app.get("/dbsetup")
def create_db(db: Session = Depends(get_db)):
    user_db.Base.metadata.drop_all(engine)
    user_db.Base.metadata.create_all(engine)
    users_repository.add_user_td(db)
    response_text = '{"message": "Database created."}'
    response = Response(content=response_text, status_code=status.HTTP_200_OK, media_type='application/json')
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)