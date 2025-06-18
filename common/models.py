from django.db import models

# Create your models here.
class CommonModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)#생성시간기준
    updated_at = models.DateTimeField(auto_now=True) 
    #생성되는 시간 기준으로 일단 생성하지만, 이후 업데이트하면 업데이트된 시간기준

    class Meta:
        abstract = True #DB 파일에 추가하는 것을 원하지 않음. 추가가 되면 복잡해짐.