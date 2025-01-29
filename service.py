from sqlalchemy.orm import Session
from typing import List
from fastapi import Request, UploadFile
import models, schemas
import boto3

import jwt

import datetime

from pathlib import Path

async def get_categories(db: Session):

    categories_all = db.query(models.Categories).order_by(models.Categories.id).all()


    import requests

    headers = {}
    
    payload = {}
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/todos/1',
        headers=headers,
        json=payload if 'params' == 'raw' else None
    )
    hello = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'categories_all': categories_all,
    }
    return res

async def get_categories_id(db: Session, id324234234234234: int):

    categories_one = db.query(models.Categories).filter(models.Categories.id == 'id').first()
    res = {
        'categories_one': categories_one,
    }
    return res

async def post_categories(db: Session, raw_data: schemas.PostCategories):
    id:str = raw_data.id
    name:str = raw_data.name
    description:str = raw_data.description


    record_to_be_added = {'id': id, 'name': name, 'description': description}
    new_categories = models.Categories(**record_to_be_added)
    db.add(new_categories)
    db.commit()
    db.refresh(new_categories)
    categories_inserted_record = new_categories


    import requests

    headers = {}
    
    payload = {'id': '1'}
    apiResponse = requests.get(
        'https://jsonplaceholder.typicode.com/posts/1',
        headers=headers,
        json=payload if 'raw' == 'raw' else None
    )
    user = apiResponse.json() if 'dict' == 'raw' else apiResponse.text
    res = {
        'categories_inserted_record': categories_inserted_record,
    }
    return res

async def put_categories_id(db: Session, raw_data: schemas.PutCategoriesId):
    id:str = raw_data.id
    name:str = raw_data.name
    description:str = raw_data.description


    categories_edited_record = db.query(models.Categories).filter(models.Categories.id == id).first()
    for key, value in {'id': id, 'name': name, 'description': description}.items():
          setattr(categories_edited_record, key, value)
    db.commit()
    db.refresh(categories_edited_record)
    categories_edited_record = categories_edited_record

    res = {
        'categories_edited_record': categories_edited_record,
    }
    return res

async def delete_categories_id(db: Session, id: int):

    categories_deleted = None
    record_to_delete = db.query(models.Categories).filter(models.Categories.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        categories_deleted = record_to_delete
    res = {
        'categories_deleted': categories_deleted,
    }
    return res

async def get_users(db: Session, raw_data: schemas.GetUsers):
    id:int = raw_data.id
    firstname:str = raw_data.firstname
    lastname:str = raw_data.lastname


    user_has_records = db.query(models.Users).filter(models.Users.firstname == 'firstname').count() > 0

    # add_variable
    user_fullname: str = "shivam"


    record_to_be_added = {'id': user_has_records.id, 'firstname': firstname, 'lastname': lastname}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    shivam = new_users

    edit_records = db.query(models.Users).filter(models.Users.id == shivam.id).first()
    for key, value in {'id': user_has_records.id, 'firstname': firstname, 'lastname': lastname}.items():
          setattr(edit_records, key, value)
    db.commit()
    db.refresh(edit_records)
    edit_records = edit_records

    res = {
        'test1': shivam,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == 'id').first()
    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, raw_data: schemas.PostUsers):
    id:int = raw_data.id
    firstname:str = raw_data.firstname
    lastname:str = raw_data.lastname


    user_has_records = db.query(models.Users).filter(models.Users.firstname == 'firstname').count() > 0

    # add_variable
    user_fullname: str = "shivam"


    record_to_be_added = {'id': user_has_records.id, 'firstname': firstname, 'lastname': lastname}
    new_users = models.Users(**record_to_be_added)
    db.add(new_users)
    db.commit()
    db.refresh(new_users)
    shivam = new_users

    edit_records = db.query(models.Users).filter(models.Users.id == shivam.id).first()
    for key, value in {'id': user_has_records.id, 'firstname': firstname, 'lastname': lastname}.items():
          setattr(edit_records, key, value)
    db.commit()
    db.refresh(edit_records)
    edit_records = edit_records

    res = {
        'test1': shivam,
    }
    return res

async def put_users_id(db: Session, raw_data: schemas.PutUsersId):
    id:str = raw_data.id
    firstname:str = raw_data.firstname
    lastname:str = raw_data.lastname


    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'firstname': firstname, 'lastname': lastname}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
        db.delete(record_to_delete)
        db.commit()
        users_deleted = record_to_delete
    res = {
        'users_deleted': users_deleted,
    }
    return res

