from fastapi import APIRouter, Response, status, Depends, HTTPException
from repository import user_repository
from sqlalchemy.orm import Session
from db_config import get_db
from schemas import UserModel, MessageModel
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


@router.get("/", response_description='Displays user by username', description='Retrieves by username', response_model=UserModel, responses={404: {"model": MessageModel}})
def get_by_username(username: str, response: Response, db: Session = Depends(get_db)):
    return_value = get_by_username(db, username)

    if return_value == None:
        return_message = 'username not found. Please check our parameter and try again'
        raise HTTPException(status_code=404, detail= return_message)
    
    response.status_code= status.HTTP_200_OK
    return return_value