from django.contrib import admin
from burgers.models import Burger

# Register your models here.
# 기초문법 정리하고싶으면 함수 데코레이터 검색해보삼 
@admin.register(Burger)
class BurgerAdmin(admin.ModelAdmin):
    pass