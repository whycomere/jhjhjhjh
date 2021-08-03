from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    #연결고리가 여러개로 되어있음 user랑 연결, CASCADE 알수없는 사용자가 데이터를적음..? 예전내용 가지고있음
    writer = models.ForeignKey(User,
                               on_delete=models.SET_NULL,
                               related_name='article',
                               null=True)

    title = models.CharField(max_length=200, null=True)
    #null=True는 없어도 괜찮다아

    image = models.ImageField(upload_to='article/', null=True)

    #CharFIeld보다 더 긴 텍스트를 사용할수있다아!!
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)


    ## 모델의 변화가 생겼기때문에 마이그래이션