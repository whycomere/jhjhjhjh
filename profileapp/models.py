from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    # user와 연결해주는거
    # cascade 는 종속을 의미하는데 유저 객체가 삭제되면 이 프로필도 삭제시킬것이다
    # 유저객체 연결시켜주는 친구
    user = models.OneToOneField(User,on_delete=models.CASCADE,
                                related_name='profile')
    #미디어 루트를 통해서 저장하는곳을 지정해줬는데 경로관련해서 사용)
    # null=True 비어이었어도 괜찮다잉!!
    image = models.ImageField(upload_to='profile/', null=True)

    nickname = models.CharField(max_length=30, unique=True,null=True)

    message = models.CharField(max_length=200, null=True)