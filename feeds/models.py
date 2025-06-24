# feeds/models.py
from django.db import models
from common.models import CommonModel

#제목, 내용, 작성자
#feed와 user의 관계
#user -> feed, feed ,feed (o)
#feed -> user, user, user (x)
#user:feed = 1:N
class Feed(CommonModel):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)

    user = models.ForeignKey("users.User", on_delete=models.CASCADE)