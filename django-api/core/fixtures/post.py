import pytest
from core.post.models import Post
from core.fixtures.user import user

@pytest.fixture
def post(db,user)->Post:
    return Post.objects.create(author=user,body="peek male ego")
