# 1. view code 작성하기
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
#이 작성한 view를 호출하기 위해서 url code를 작성해야한다.