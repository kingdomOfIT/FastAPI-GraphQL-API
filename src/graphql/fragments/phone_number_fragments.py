import strawberry

# from ..scalars.phone_number_scalar import PhoneNumberNotFound, PhoneNumberDeleted, PhoneNumberResponse
from src.graphql.scalars.phone_number_scalar import *
from src.graphql.scalars.user_scalar import UserNameMissing, UserNotFound


CreatePhoneNumberResponse = strawberry.union("CreatePhoneNumberResponse", (PhoneNumberResponse, UserNotFound, UserNameMissing))
UpdatePhoneNumberResponse = strawberry.union("UpdatePhoneNumberResponse", (PhoneNumberResponse, PhoneNumberNotFound))
DeletePhoneNumberResponse = strawberry.union("DeletePhoneNumberResponse", (PhoneNumberDeleted, PhoneNumberNotFound))