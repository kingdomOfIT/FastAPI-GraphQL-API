from tests.conftest import TestAsynchronously
from .mutations import *
from .queries import *

from src.app import schema

class TestUsers(TestAsynchronously):

    def test_01_an_async_list_all_users(self):
        resp = self.get_async_result(schema.execute(
            listUsers,
        ))
        assert resp.data["listUsers"] == []

    def test_02_an_async_create_users(self):
        resp = self.get_async_result(schema.execute(
            createUser,
        ))
        assert resp.data["CreateUser"] == {'id': 1, 'name': 'test'}

    def test_03_an_async_create_user_again(self):
        resp = self.get_async_result(schema.execute(
            createUser,
        ))
        assert resp.data == {'CreateUser': {'message': 'User with this name already exists'}}

    def test_04_an_async_create_phone_number_relative_to_user(self):
        resp = self.get_async_result(schema.execute(
            createPhoneNumber,
        ))

        for key_phone_number in resp.data['PhoneNumberResponse'].keys():
            assert key_phone_number in ['id','createdAt', 'updatedAt','name','userID', 'phoneNumber'] 

    def test_05_an_async_list_all_users_with_created_user(self):
        resp = self.get_async_result(schema.execute(
            listUsers,
        ))
        assert len(resp.data["listUsers"]) == 1
        for key_user in resp.data["listUsers"][0].keys():
            assert key_user in ['id','name','phoneNumber']

        for key_phone_number in resp.data["users"][0]['phoneNumber'][0].keys():
            assert key_phone_number in ['id','createdAt', 'updatedAt','name','userID', 'phoneNumber'] 

    def test_06_an_async_get_specific_user(self):
        resp = self.get_async_result(schema.execute(
            getUser,
        ))
        for key_user in resp.data["user"].keys():
            assert key_user in ['id','name','phoneNumber'] 
      
        for key_phone_number in resp.data["user"]['phoneNumber'][0].keys():
            assert key_phone_number in ['id', 'createdAt', 'updatedAt', 'name', 'userID', 'phoneNumber']

    def test_07_an_async_get_all_phone_numbers(self):
        resp = self.get_async_result(schema.execute(
            listUsers,
        ))

        assert len(resp.data["phoneNumber"]) == 1
        for key_phone_number in resp.data['phoneNumber'][0].keys():
            assert key_phone_number in ['id','createdAt', 'updatedAt','name','userID', 'phoneNumber']
    
    def test_08_an_async_get_specific_phone_number(self):
        resp = self.get_async_result(schema.execute(
            getPhoneNumber,
        ))

        for key_phone_number in resp.data['phoneNumber'].keys():
            assert key_phone_number in ['id','createdAt', 'updatedAt','name','userID', 'phoneNumber']

    def test_09_an_async_update_specific_phone_number(self):
        resp = self.get_async_result(schema.execute(
            updatePhoneNumber,
            variable_values={
            "id": 1,
            "name": "new text",
            "phoneNumber": "new text",
            }
        ))

        assert resp.data["updatedPhoneNumber"]["text"] == "new text"
        assert resp.data["updatedPhoneNumber"]["text"] == "new text"
        for key_phone_number in resp.data["updatedPhoneNumber"].keys():
            assert key_phone_number in ['id','createdAt', 'updatedAt','name','userID', 'phoneNumber']

    def test_10_an_async_delete_specific_phone_number(self):
        resp = self.get_async_result(schema.execute(
            deletePhoneNumber,
        ))

        assert resp.data == {"deletePhoneNumber": {"message": "PhoneNumber deleted"}}

        resp = self.get_async_result(schema.execute(
            deletePhoneNumber,
        ))
        assert resp.data == {"deletePhoneNumber": { "message": "Couldn't find Phone Number with the supplied id"}}

    def test_11_an_async_delete_specific_user(self):
        resp = self.get_async_result(schema.execute(
            deleteUser,
        ))
        assert resp.data == {"deleteUser": {"message": "User deleted"}}
        resp = self.get_async_result(schema.execute(
            deleteUser,
        ))
        assert resp.data == {"deleteUser": { "message": "Couldn't find user with the supplied id"}}
    
    def test_12_an_async_list_all_users(self):
        resp = self.get_async_result(schema.execute(
            listUsers,
        ))
        assert resp.data["users"] == []