"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# 3. 최상위 url conf에 polls url 연결.
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),#include는 다른 url conf를 참조할 수 있게 함.
    path('admin/', admin.site.urls),
]

# 우리가 이때까지 한 것. 
# 1. 만약 127.0.0.1/polls/라는 url이 들어왔다고 치면 이 url을 parsing해서 polls라는 path를 잡아내고 polls앱 url로 연결
# 2. polls앱 내부에서는 /polls/만 들어와버리니까 아무 정보가 없음. 그래서 앱 내에서 views.index부분에 의해 views 내부로 연결
# 3. views앱 내부에서는 "Hello, world. You're at the polls index."라는 것을 client한테 전달을 해주는 것.