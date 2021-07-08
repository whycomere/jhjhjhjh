from django.db import models

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)

# null = false 이유는 텍스트가하나밖에없어서 다 사라질수도 있다잉