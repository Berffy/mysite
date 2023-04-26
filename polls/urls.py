# 2. url code 작성하기
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
#다음은 최상위 url conf에 polls앱 url를 연결하기. 최상위 url conf는 mysite의 urls.py에 위치.