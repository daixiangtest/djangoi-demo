import time

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import NewsInfo
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


# Create your views here.

# 试图函数存放具体调用方法，当服务启动时，同urls文件里的路径可以调用对应的方法
def index(request):
    return HttpResponse("<h1>这是index路径<h1>")


# 获取数据的数据进行展示
def list1(request):
    dbs = NewsInfo.objects.all()
    list1 = ''
    for item in dbs:
        data = f"<h1>{item.title}+{item.content}+{item.b_date}<h1>"
        list1 += data
    return HttpResponse(list1)


def list2(request):
    """
    1.模板文件存放在templates文件夹中，并在项目文件的settings.py中配置文件路径
    2。创建html模板文件页面
    3.视图函数中调用render（）方法返回html文件，数据库数据做作为入参传入render（）函数中然后在HTML文件中使用 {{变量名}} 引用变量即可
    4.定义试图的路由

    :param request:
    :return:
    """
    db = NewsInfo.objects.all()[0]
    dict1 = {"title": db.title,
             "content": db.content,
             "b_date": db.b_date,
             "read": db.read}
    # render函数接受静态页面文件与dict1的字典数据
    return render(request, 'news/list.html', dict1)


# name为url中的路径参数
def user(request, name):
    return HttpResponse(f"你好{name}欢迎访问我的django")


# name为url路径中的变量名参数
def user2(request, name1):
    return HttpResponse(f"你好{name1}欢迎访问我的django")


# 所有的请求参数都是存放在request中通过字段方法来获取请求值
def demo01(request):
    path = request.path
    method = request.method
    post = request.POST
    get = request.GET
    print(f"路径：{path}\n请求方法：{method}\npost数据：{str(post)}\nget数据：{str(get)}")
    return render(request, 'news/demo01.html')


# 获取post请求值
def demo02(request):
    data = request.POST
    datas = {}
    if data:
        print(data)
        # 获取post请求值将请求体中的name字段赋值给name将password请求字段的值赋值给password
        datas["name"] = data['name']
        datas["password"] = data['password']

    return render(request, 'news/demo02.html', datas)


def demo3(request):
    # 通过response对象可以设置接口的cookie信息
    # res = HttpResponse("cookie信息")
    # res.set_cookie("token", value='abcd123456')
    # return res
    # json_response是response的一个子类对象用来返回一个json数据格式
    json_res = JsonResponse({"status": "succes", "code": 200})
    # 添加并设置cookie
    json_res.set_cookie("token", value='abcd123456')
    # 删除cookie
    # json_res.delete_cookie("token")
    return json_res


def demo4(request):
    # 重定向接口可以引用django的redirect类来实现
    return redirect("/news/demo2/")


# 试图类定义，可以通过不同的请求方法来实现不同的功能
class NewsView(View):
    def get(self, request):
        # 查询数据库信息
        datas = NewsInfo.objects.all()
        res = []
        for data in datas:
            item = dict(title=data.title, content=data.content)
            res.append(item)
        return JsonResponse(res, safe=False)

    def post(self, request):
        # 添加数据库信息
        db = NewsInfo.objects
        data = request.POST
        print(data)
        if data:
            db.create(title=data["title"], content=data['content'], b_date='2024-08-01', read='2', comment='3')
        return JsonResponse({'status': 'success'})


# session 存储
def session_demo(request):
    # request.session['nums'] = 30000
    a = request.session.get('nums')
    print(a)
    return HttpResponse('写入session')


# 模板的变量
def demo001(request):
    name = "xiaohua"
    age = 18
    chengji = {"语文": 99, "数学": 88, "英语": 86}
    list = [11, 22, 33, 44, 55, 66]
    date = "2015-66-32"
    context = locals()
    return render(request, "news/demo001.html", context)


# 模板的继承
def demo002(request):
    # 模板过滤器
    title = '模板继承'
    new_list = NewsInfo.objects.all()

    return render(request, 'news/temp3.html', locals())


def demo003(request):
    # 静态文件调用
    return render(request, 'news/static.html')


class uesr_demo(View):
    def get(self, request):
        # 创建用户
        data = request.GET
        # 注册用户
        user = User.objects.create_user(username=data["user"], password=data['passwd'])
        # 保存用户
        user.save()
        return render(request, "news/setpwd.html")

    def post(self, request):
        data = request.POST
        # 查询需要更改的用户名
        user = User.objects.get(username=data['name'])
        # 更改用户密码
        user.set_password(data['password'])
        return JsonResponse({"code": 200, "status": "succeed"})


class loginDemo(View):
    def get(self, request):
        return render(request, 'news/login.html')

    def post(self, request):
        data = request.POST
        # django内置的校验方法，校验用户名和密码，如果失败返回空数据
        res = authenticate(request, username=data['name'], password=data['password'])
        if res is not None:
            # 校验成功就将用户信息保存到session中
            login(request, res)
            return JsonResponse({'message': "succeed"})
        else:
            return JsonResponse({'message': "error"}, status=400)
