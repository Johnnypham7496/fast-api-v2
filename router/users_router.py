from fastapi import APIRouter, Response, status, Depends
from repository import user_repository
from sqlalchemy.orm import Session
from db_config import get_db
from schemas import UserModel
from typing import List


router = APIRouter(
    prefix= "/users/v1",
    tags= ["users"]
)


@router.get("/", response_description="Displays all users", description="Retrieves all users", response_model=List[UserModel])
def get_users(response: Response, db: Session = Depends(get_db)):
    return_value = user_repository.get_all_users(db)
    response.status_code = status.HTTP_200_OK
    return return_value