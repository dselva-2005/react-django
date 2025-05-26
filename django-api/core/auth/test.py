import pytest
from core.fixtures.user import user
from rest_framework import status


class TestAuthenticationVieset:
    endpoint = "/api/auth/"

    def test_login(self, client, user):
        data = {"email": user.email, "password": "dselvajagan2005"}
        response = client.post(self.endpoint + "login", data, format="json")
        print(response.data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
        assert response.data["user"]["id"] == user.public_id.hex
        assert response.data["user"]["username"] == user.username
        assert response.data["user"]["email"] == user.email

    @pytest.mark.django_db
    def test_register(self, client):
        data = {
            "username": "dselva",
            "email": "dselvajagan@gmail.com",
            "first_name": "dselva",
            "last_name": "jagan",
            "password": "dselva2005",
        }

        response = client.post(self.endpoint + "register", data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_refrest(self, client, user):
        data = {"email": user.email, "password": "dselvajagan2005"}

        response = client.post(self.endpoint + "login", data)

        assert response.status_code == status.HTTP_200_OK

        data_refresh = {"refresh": response.data["refresh"]}
        response = client.post(self.endpoint + "refresh", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
