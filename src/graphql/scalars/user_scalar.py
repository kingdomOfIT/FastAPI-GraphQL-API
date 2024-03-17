import strawberry
from pydantic import Field, typing
# from ..scalars.phone_number_scalar import PhoneNumberResponse
from src.graphql.scalars.phone_number_scalar import PhoneNumberResponse

@strawberry.type
class User:
    id: int
    name: typing.Optional[str] = ""
    phoneNumber: typing.Optional[typing.List[PhoneNumberResponse]] = Field(default_factory=list)

@strawberry.type
class CreateUser:
    id: int
    name: typing.Optional[str] = ""

@strawberry.type
class UserExists:
    message: str = "User with this name already exists"

@strawberry.type
class UserNotFound:
    message: str = "Couldn't find user with the supplied id"

@strawberry.type
class UserNameMissing:
    message: str = "Please supply user name"

@strawberry.type
class UserIdMissing:
    message: str = "Please supply user id"

@strawberry.type
class UserDeleted:
    message: str = "User deleted"

