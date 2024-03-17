listUsers = """
query MyQuery {
  listUsers {
    id
    name
    phoneNumber {
      userID
      updatedAt
      phoneNumber
      id
      name
      createdAt
    }
  }
}
"""

getUser = """
query MyQuery2 {
  getUser(userId: 1) {
    id
    name
    phoneNumber {
      createdAt
      updatedAt
      id
      name
      phoneNumber
      userID
    }
  }
}
"""

listPhoneNumbers = """
query MyQuery3 {
  listPhoneNumbers {
    createdAt
    updatedAt
    id
    name
    phoneNumber
    userID
  }
}
"""

getPhoneNumber = """
query MyQuery4 {
  getPhoneNumber(id: 1) {
    createdDatetime
    createdAt
    updatedAt
    id
    name
    phoneNumber
    userID
  }
}"""