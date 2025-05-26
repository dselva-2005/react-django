import pytest
from core.fixtures.user import user
from core.fixtures.post import post
from core.comment.models import Comment


@pytest.mark.django_db
def test_comment_creation(user, post):
    comment = Comment.objects.create(
        author=user, post=post, body="this is the comment for a post"
    )
    assert comment.body == "this is the comment for a post"
    assert comment.author == user
    assert comment.post == post
