createUser = """
    mutation MyMutation {
        createUser(name: "test") {
            ... on CreateUser {
            id
            name
            }
            ... on UserExists {
            message
            }
        }
    }
"""

createPhoneNumber = """
mutation MyMutation {
  createPhoneNumber(name: "Contact text", phoneNumber: "+992888832", userId: 1) {
    ... on PhoneNumberResponse {
      id
      createdAt
      name
      phoneNumber
      userId
    }
    ... on UserNotFound {
      message
    }
    ... on UserNameMissing {
      message
    }
  }
}
"""

deleteUser = """
mutation MyMutation {
  deleteUser(userId: 1) {
    ... on UserDeleted {
      message
    }
    ... on UserNotFound {
      message
    }
    ... on UserIdMissing {
      message
    }
  }
}
"""

updatePhoneNumber = """
mutation MyMutation3 {
  updatePhoneNumber(id: 1, name: "DiffName", phoneNumber: "+123123123") {
    ... on PhoneNumberResponse {
      id
      createdAt
      updatedAt
      name
      userID
      phoneNumber
    }
    ... on PhoneNumberNotFound {
      message
    }
  }
}"""

deletePhoneNumber = """
mutation MyMutation4 {
  deletePhoneNumber(id: 1) {
    ... on PhoneNumberDeleted {
      message
    }
    ... on PhoneNumberNotFound {
      message
    }
  }
}
"""