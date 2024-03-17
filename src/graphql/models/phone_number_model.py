from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from typing import Optional
from . import Base, User

class PhoneNumber(Base):
    __tablename__ = "phonenumber"
    id: int = Column(Integer, primary_key=True, index=True)
    name: str = Column(String, nullable=True)
    phoneNumber: str = Column(String, nullable=True)
    createdAt: DateTime = Column(DateTime, nullable=False)
    updatedAt: DateTime = Column(DateTime, nullable=False)
    userID: Optional[int] = Column(Integer, ForeignKey(User.id, ondelete='CASCADE'), nullable=True)

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "phoneNumber": self.phoneNumber,
            "createdAt": self.createdAt,
            "updatedAt": self.updatedAt,
            "userID": self.userID
        }