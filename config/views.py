# -*- coding:utf-8 -*-
# 주문을 처리하는 직원
# 백엔드 영역

# from django.http import HttpResponse 처음에만 이렇게 하고 앞으로 이렇게 쓸 일이 없다.
from django.shortcuts import render

def main(request):
    #return HttpResponse("안녕하세요, pyburger입니다.") # 오후에 이  코드를 HTML로 처리할 것.
    return render(request, "main.html")

#p.48
def burger_list(request):
    #return HttpResponse("pyburger의 햄버거 목록입니다.")
    return render(request, "burger_list.html")