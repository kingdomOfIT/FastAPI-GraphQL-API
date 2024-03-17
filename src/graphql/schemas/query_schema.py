import strawberry
from pydantic import typing
from strawberry.types import Info
from ..scalars.phone_number_scalar import PhoneNumberResponse

from ..resolvers.phone_number_resolver import getPhoneNumber, listPhoneNumbers
from src.graphql.resolvers.user_resolver import getUser, listUsers
from src.graphql.scalars.user_scalar import User

@strawberry.type
class Query:

    @strawberry.field
    async def listUsers(self, info:Info) -> typing.List[User]:
        """ List all users """

        users_data_list = await listUsers(info)
        return users_data_list

    @strawberry.field
    async def getUser(self, info:Info, userID: int) -> User:
        """ Get user by id """

        user_dict = await getUser(userID, info)
        return user_dict

    @strawberry.field
    async def listPhoneNumbers(self, info:Info) -> typing.List[PhoneNumberResponse]:
        """ List all phone_number """
        listPNResponse = await listPhoneNumbers(info)
        return listPNResponse

    @strawberry.field
    async def getPhoneNumber(self, info:Info, id: int) -> PhoneNumberResponse:
        """ Get Phone Number by id """
        getPNResponse = await getPhoneNumber(id, info)
        return getPNResponse