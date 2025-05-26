from rest_framework import status
from core.fixtures.user import user
from core.fixtures.post import post

class TestPostViewset:
    endpoint = '/api/post'

    def test_list(self,client,user,post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1

    