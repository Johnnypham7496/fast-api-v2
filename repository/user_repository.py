from sqlalchemy.orm.session import Session
from db.user_db import UserDb



def get_all_users(db: Session):
    return db.query(UserDb).all()


def get_by_username(db: Session, _username):
    query = db.query(UserDb).filter(UserDb.username==_username).first()
    return query


def get_by_email(db: Session, _email):
    query = db.query(UserDb).filter(UserDb.email== _email).first()
    return query


def add_user(db: Session, _username, _email, _role):
    new_user = UserDb(username = _username, email = _email, role = _role)
    db.add(new_user)
    db.commit()
    # refresh allows for retrieval of id that was just created
    db.refresh(new_user)
    return new_user


def add_user_td(db: Session):
    add_user(db, "darth.vader", "darth.vader@gmail.com", "villain")
    add_user(db, "super.man", "superman@gmail.com", "hero")
    add_user(db, "thor", "thor.odinson@gmail.com", "hero")


def update_user(db: Session, _username, _email, _role):
    user_to_update = db.query(UserDb).filter(UserDb.username== _username).first()

    if _email != '':
        user_to_update.email = _email

    if _role != '':
        user_to_update.role = _role

    db.commit()


def delete_user(db: Session, _username):
    db.query(UserDb).filter(UserDb.username == _username).delete()
    db.commit()
    