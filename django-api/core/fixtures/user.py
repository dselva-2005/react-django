import pytest
from core.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@gmail.com",
    "first_name": "dselva",
    "last_name": "jagan",
    "password": "dselvajagan2005",
}

@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)
