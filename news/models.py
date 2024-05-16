from django.db import models


# Create your models here.

# 创建一个类来管理数据表类名为表名类属性为字段名
# 类名必须继承models类
class NewsInfo(models.Model):
    """
    title为标题：字符串格式最大长度为30
    content为新闻内容 为文本格式
    b_date为时间  为时间格式
    read 为阅读量 为整数
    """
    title = models.CharField(max_length=30)
    content = models.TextField()
    b_date = models.DateField()
    read = models.IntegerField()

# 类名创建完成生成迁移文件 ：python manage.py makemigrations
# 根据生成的迁移文件在数据库中创建表 python manage.py migrate
