from django.contrib import admin
from .models import NewsInfo, NewsType


# Register your models here.

# 注册模型类
# 运行 python manage.py createsuperuser 创建超级用户
# admin.site.register(NewsInfo)


# 自定义展示模型类的字段
class NewsIndoAdmin(admin.ModelAdmin):
    list_display = ['id', "title", "b_date"]


class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ["id", 'type']


# 将自定义数据展示的重新注册
admin.site.register(NewsInfo, NewsIndoAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
