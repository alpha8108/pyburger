from django.db import models

# Create your models here.
class Burger(models.Model):# 모델 클래스 정의
    name = models.CharField(max_length=20) # 문자열 저장
    price = models.IntegerField(default=0) # 숫자 저장
    calories = models.IntegerField(default=0) # 숫자 저장 데이터베이스 세팅을 한거고 업로드는 안한 상태. 이제 시켜줘야함.

    def __str__(self):return self.name