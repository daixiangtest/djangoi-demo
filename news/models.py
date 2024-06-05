from django.db import models

# Create your models here.

# 创建一个类来管理数据表类名为表名类属性为字段名
# 类名必须继承models类

"""
数据表之间的关联有以下三种
    一对一： OneToOneField: 一对一可以将字段定义在任意一端的表中
    一对多： ForeignKey:  一对多将字段定义在字段多的表中
    多对多： ManyToManyField: 多对多将字段定义在任意一端中 
"""


class NewsInfo(models.Model):
    """
    title为标题：字符串格式最大长度为30
    content为新闻内容 为文本格式
    b_date为时间  为时间格式
    read 为阅读量 为整数
    comment 评论数量
    """
    title = models.CharField(max_length=30, verbose_name='标题1', help_text='标题2')
    content = models.TextField(verbose_name='文本1', help_text='文本2')
    b_date = models.DateField(verbose_name='时间', help_text='时间2')
    read = models.IntegerField(verbose_name='阅读量1', help_text='阅读量2')
    comment = models.IntegerField(verbose_name='评论数1', help_text='评论数2')

    class Meta:
        # Meta类声明表的的一些属性，db_table为表起名
        db_table = 'news'
        # 在后台管理中展示的表名称
        verbose_name = '新闻信息表'

    def __str__(self):
        # 默认展示表中的title字段
        return self.title


# 类名创建完成生成迁移文件 ：python manage.py makemigrations
# 根据生成的迁移文件在数据库中创建表 python manage.py migrate

class NewsType(models.Model):
    """
    type 新闻类型
    """
    type = models.CharField(max_length=20, verbose_name='类型1', help_text='类型2')
    # 表示该表与NewsInfo表关联是多对多的关系
    news = models.ManyToManyField('NewsInfo', verbose_name='多对多1', help_text='多对多2')

    class Meta:
        db_table = 'type'
        verbose_name = '新闻类型表'

    def __str__(self):
        return self.type
