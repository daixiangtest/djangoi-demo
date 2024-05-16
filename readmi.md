# 目录解释
- manage.py: 一个让你用各种方式管理Django项目的命令行工具。
- settings.py: 是项目的整体配置文件。
- urls.py: 是项目的URL配置文件。
- wsgi.py：作为你的项目的运行在WSGI兼容的Web服务器上的入口。
- asgi.py：作为你的项目的运行在ASGI兼容的Web服务器上的入口
## 创建应用及目录解析
>  python manage.py startapp 应用名
- tests.py文件用于开发测试用例,在实际开发中会有专门的测试人员，这个事情不需要我们来做。  
- models.py文件跟数据库操作相关。  
- views.py文件跟接收浏览器请求，进行处理，返回页面相关。  
- admin.py文件跟网站的后台管理相关。  
- migrations文件夹生成迁移文件。  