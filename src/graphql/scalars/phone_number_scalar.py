from datetime import datetime
from pydantic import Field, typing
import strawberry

@strawberry.type
class PhoneNumberResponse:
    id: int
    name: typing.Optional[str] = ""
    phoneNumber: typing.Optional[str] = ""
    createdAt : typing.Optional[datetime] = Field(default_factory=datetime.now)
    updatedAt : typing.Optional[datetime] = Field(default_factory=datetime.now)
    userID: typing.Optional[int] = Field(description="User id")

@strawberry.type
class PhoneNumberNotFound:
    message: str = "Couldn't find Phone Number with the supplied id"

@strawberry.type
class PhoneNumberDeleted:
    message: str = "Phone Number deleted"

