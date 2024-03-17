from datetime import datetime
# from ..models import PhoneNumber
from src.graphql.models import PhoneNumber
from sqlalchemy import delete, select, update
from sqlalchemy.orm import load_only

from src.graphql.helpers.helper import getOnlySelectedFields, getValidData
# from ..db.session import get_session
from src.graphql.db.session import get_session
from src.graphql.models import user_model
# from ..scalars.phone_number_scalar import PhoneNumberDeleted, PhoneNumberNotFound, PhoneNumberResponse
from src.graphql.scalars.phone_number_scalar import *
from src.graphql.scalars.user_scalar import UserNotFound

async def listPhoneNumbers(info):
    """ Get all phonenumbers resolver """

    selectedFields = getOnlySelectedFields(PhoneNumber, info)

    async with get_session() as s:
        # Select only the columns specified in selectedFields
        columns = [getattr(PhoneNumber, field) for field in selectedFields]
        sql = select(*columns).order_by(PhoneNumber.id)

        dbPhoneNumbers = (await s.execute(sql)).all()

    phoneNumberDataList = []
    for phoneNumber in dbPhoneNumbers:
        # Construct PhoneNumberResponse objects with selected data
        phoneNumberData = {field: getattr(phoneNumber, field) for field in selectedFields}
        phoneNumberResponse = PhoneNumberResponse(**phoneNumberData)
        phoneNumberDataList.append(phoneNumberResponse)

    return phoneNumberDataList


async def getPhoneNumber(id, info):

    """ Get specific Phone Number by id resolver """

    selected_fields = getOnlySelectedFields(PhoneNumber,info)

    async with get_session() as s:

        sql = select(PhoneNumber).filter(PhoneNumber.id == id).order_by(PhoneNumber.name)

        db_phoneNumber = (await s.execute(sql)).scalars().unique().one()
    
    phone_number_dict = getValidData(db_phoneNumber, PhoneNumber)
    return PhoneNumber(**phone_number_dict)

async def createPhoneNumber(name, userID, phoneNumber):

    """ Create Phone number resolver """

    async with get_session() as s:
        db_user = None
        sql = select(user_model.User).where(user_model.User.id == int(userID))
        db_user = (await s.execute(sql)).scalars().first()
        if not db_user:
            return UserNotFound()
        dbPhoneNumbers = PhoneNumber(name=name, phoneNumber=phoneNumber, createdAt=datetime.now(), updatedAt=datetime.now(), userID=db_user.id)
        s.add(dbPhoneNumbers)
        await s.commit()

    dbPhoneNumberSerializerData = dbPhoneNumbers.as_dict()

    return PhoneNumberResponse(**dbPhoneNumberSerializerData)

async def deletePhoneNumber(id):

    """ Delete Phone Number resolver """

    async with get_session() as s:

        sql = select(PhoneNumber).where(PhoneNumber.id == id)
        existingDbPhoneNumber = (await s.execute(sql)).first()

        if existingDbPhoneNumber is None:
            return PhoneNumberNotFound()

        query =  delete(PhoneNumber).where(PhoneNumber.id == id)
        await s.execute(query)
        await s.commit()
    
    return PhoneNumberDeleted()

async def updatePhoneNumber(id, name, phoneNumber):

    """ Update Phone Number resolver """

    async with get_session() as s:
        sql = select(PhoneNumber).where(PhoneNumber.id == id)
        existingDbPhoneNumber = (await s.execute(sql)).first()
        if existingDbPhoneNumber is None:
            return PhoneNumberNotFound()

        query = update(PhoneNumber).where(PhoneNumber.id == id).values(name=name, phoneNumber=phoneNumber)
        await s.execute(query)

        sql = select(PhoneNumber).where(PhoneNumber.id == id)
        dbPhoneNumber = (await s.execute(sql)).scalars().unique().one()
        await s.commit()

    dbPhoneNumberSerializer = dbPhoneNumber.as_dict()
    return PhoneNumberResponse(**dbPhoneNumberSerializer)