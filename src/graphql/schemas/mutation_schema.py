import strawberry

# from ..resolvers.phone_number_resolver import createPhoneNumber, updatePhoneNumber, deletePhoneNumber
from src.graphql.resolvers.phone_number_resolver import *
from src.graphql.resolvers.user_resolver import createUser, deleteUser
# from ..fragments.phone_number_fragments import CreatePhoneNumberResponse, DeletePhoneNumberResponse, UpdatePhoneNumberResponse
from src.graphql.fragments.phone_number_fragments import *
from src.graphql.fragments.user_fragments import CreateUserResponse, DeleteUserResponse


@strawberry.type
class Mutation:

    @strawberry.mutation
    async def createPhoneNumber(self, name: str, phoneNumber: str, userID: int) -> CreatePhoneNumberResponse:
        """ Create Phone Number """
        createPNResponse = await createPhoneNumber(name, userID, phoneNumber)
        return createPNResponse

    @strawberry.mutation
    async def createUser(self, name: str) -> CreateUserResponse:
        """ Create user """
        createUserResponse = await createUser(name)
        return createUserResponse

    @strawberry.mutation
    async def deleteUser(self, user_id: int) -> DeleteUserResponse:
        """ Delete user """
        deleteUserResponse = await deleteUser(user_id)
        return deleteUserResponse

    @strawberry.mutation
    async def deletePhoneNumber(self, id: int) -> DeletePhoneNumberResponse:
        """ Delete Phone Number """
        deletePNResponse = await deletePhoneNumber(id)
        return deletePNResponse

    @strawberry.mutation
    async def updatePhoneNumber(self, id: int, name: str, phoneNumber: str,) -> UpdatePhoneNumberResponse:
        """ Update Phone Number """
        updatePNResponse = await updatePhoneNumber(id, name, phoneNumber)
        return updatePNResponse