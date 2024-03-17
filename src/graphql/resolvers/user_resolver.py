from sqlalchemy import delete, insert, select
from sqlalchemy.orm import subqueryload

from ..db.session import get_session
from src.graphql.helpers.helper import getOnlySelectedFields, getValidData
from src.graphql.models import user_model
from src.graphql.scalars.user_scalar import CreateUser, User, UserDeleted, UserExists, UserNotFound


async def listUsers(info):
    """ List all users resolver """

    selected_fields = getOnlySelectedFields(user_model.User, info)

    async with get_session() as s:
        sql = select(user_model.User).options(subqueryload(user_model.User.phoneNumber)).order_by(user_model.User.name)

        db_users = (await s.execute(sql)).scalars().unique().all()

    users_data_list = []
    for user in db_users:
        user_dict = getValidData(user,user_model.User)
        user_dict["phoneNumber"] = user.phoneNumber
        users_data_list.append(User(**user_dict))

    return users_data_list

async def getUser(user_id, info):
    """ Get specific user by id resolver """
    selected_fields = getOnlySelectedFields(user_model.User,info)

    async with get_session() as s:

        sql = select(user_model.User).options(subqueryload(user_model.User.phoneNumber)) \
        .filter(user_model.User.id == user_id).order_by(user_model.User.name)

        db_user = (await s.execute(sql)).scalars().unique().one()
    
    user_dict = getValidData(db_user,user_model.User)
    user_dict["phoneNumber"] = db_user.phoneNumber
    return User(**user_dict)

async def createUser(name):
    """ Add user resolver """

    async with get_session() as s:
        sql = select(user_model.User.name).filter(user_model.User.name == name)
        
        print("================================")
        print("SQL: ", sql)
        print("================================")
        
        existingDbUser = (await s.execute(sql)).first()

        if existingDbUser is not None:
            return UserExists()

        query = insert(user_model.User).values(name=name)
        await s.execute(query)
        
        sql = select(user_model.User).filter(user_model.User.name == name)
        db_user = (await s.execute(sql)).scalars().unique().one()
        await s.commit()

    db_user_serialize_data = db_user.as_dict()
    return CreateUser(**db_user_serialize_data)


async def deleteUser(user_id):
    """ Delete user resolver """
    
    async with get_session() as s:
        sql = select(user_model.User).where(user_model.User.id == user_id)
        existingDbUser = (await s.execute(sql)).first()
        if existingDbUser is None:
            return UserNotFound()

        query = delete(user_model.User).where(user_model.User.id == user_id)
        await s.execute(query)
        await s.commit()
    
    return UserDeleted()