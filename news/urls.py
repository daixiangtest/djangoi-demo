"""
URL configuration for djangoProjectTest project.

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

from django.urls import path, re_path
from .views import *

urlpatterns = [
    # 如果访问的是news下面的index路径则调用index方法
    path('index/', index),
    path('list1/', list1),
    path('list2/', list2),
    # 正则提取（）中的规范为路径参数按照位置顺序进入视图函数中
    re_path(r"^user/(\d+)/$", user),
    # 使用（？P<变量名>数据规范）接受的路径参数赋值到变量中
    re_path(r"^user2/(?P<name1>\d+)/$", user2),
    path("demo1/", demo01),
    path('demo2/', demo02),
    path("demo3/", demo3),
    path('demo4/', demo4),
    path('view/', NewsView.as_view()),  # 类试图需要.as_view()方法
    path('session/', session_demo),
    path("demo001/", demo001),
    path("demo002/", demo002),
    path("demo003/", demo003),
    path("user/", uesr_demo.as_view()),
    path('login/', loginDemo.as_view())

]
