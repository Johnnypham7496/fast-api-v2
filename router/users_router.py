from fastapi import APIRouter, Response, status, Depends, HTTPException
from repository import user_repository
from sqlalchemy.orm import Session
from db_config import get_db
from schemas import UserModel, MessageModel,CreateUserModel, UpdateUserModel
from typing import List


router = APIRouter(
    prefix= "/users/v1",
    tags= ["users"]
)


@router.get("/", response_description="Displays all users", description="Retrieves all users", response_model=List[UserModel])
def get_all_users(response: Response, db: Session = Depends(get_db)):
    return_value = user_repository.get_all_users(db)
    response.status_code = status.HTTP_200_OK
    return return_value


@router.get("/{username}", response_description='Displays user by username', description='Retrieves by username', response_model=UserModel, responses={404: {"model": MessageModel}})
def get_by_username(username: str, response: Response, db: Session = Depends(get_db)):
    return_value = user_repository.get_by_username(db, username)

    if return_value == None:
        return_message = 'username not found. Please check your parameter and try again'
        raise HTTPException(status_code=404, detail= return_message)
    
    response.headers['Detail'] = 'User found'
    response.status_code= status.HTTP_200_OK
    return return_value


@router.post("/", response_description='Successfully created a user', description='Creates a user')
def create_user(request: CreateUserModel, response: Response, db: Session = Depends(get_db)):
    username_request = request.username
    email_request = request.email
    role_request = request.role

    existing_username = user_repository.get_by_username(db, username_request)
    existing_email = user_repository.get_by_email(db, email_request) 

    if existing_username:
        response_text = 'username already exists. Please check your payload and try again'
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=response_text)
    
    if existing_email:
        response_text = 'email already exists. Please check your payload and try again'
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=response_text)
    
    if username_request.strip() == '':
        response_text = 'username field cannot be empty. Please check your payload and try again'
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response_text)
    
    if email_request.strip() == '':
        response_text = 'email field cannot be empty. Please check your payload and try again'
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response_text)

    if role_request.strip() == '':
        response_text = 'role field cannot be empty. Please check your payload and try again'
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST, detail= response_text)
    

    response.status_code = status.HTTP_201_CREATED
    response.headers['Location'] = '/users/v1' + str(username_request.strip())
    return user_repository.add_user(db, username_request.strip(), email_request.strip(), role_request.strip())


@router.put('/{username}', response_description='Successfully updated user info', description='Updating user record', status_code=status.HTTP_204_NO_CONTENT, responses= {status.HTTP_204_NO_CONTENT: {"model": None}, status.HTTP_400_BAD_REQUEST: {'model': MessageModel}, status.HTTP_404_NOT_FOUND: {'model': MessageModel}})
def update_user(username: str, request: UpdateUserModel, response: Response, db: Session = Depends(get_db)):
    email_request = request.email
    role_request = request.role


    if not email_request and not role_request:
        response_text = 'request body cannot be empty. Please check your payload and try again.'
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= response_text)
    
    user_check = user_repository.get_by_username(db, username)

    if not user_check:
        response_text = 'username already exists. Please check your parameter and try again.'
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=response_text)
    
    if email_request: 
        email_request = email_request.strip()
    else:
        email_request = ''

    if role_request:
        role_request = role_request.strip()
    else:
        email_request = ''

    if email_request == '' and role_request == '':
        response_text = 'request body fields cannot be empty. Please check your payload and try again.'
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=response_text)
    

    response.status_code = status.HTTP_204_NO_CONTENT
    return user_repository.update_user(db, username, email_request, role_request)