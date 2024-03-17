import strawberry

from src.graphql.scalars.user_scalar import CreateUser, UserDeleted, UserExists, UserIdMissing, UserNotFound


CreateUserResponse = strawberry.union("CreateUserResponse", (CreateUser, UserExists))
DeleteUserResponse = strawberry.union("DeleteUserResponse", (UserDeleted,UserNotFound, UserIdMissing))