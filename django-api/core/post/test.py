import pytest
from core.fixtures.user import user
from core.post.models import Post


@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user,body='the king')
    assert post.body == 'the king'
    assert post.author == user