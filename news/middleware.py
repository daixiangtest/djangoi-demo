from django.utils.deprecation import MiddlewareMixin

"""
Django中的中间件是一个轻量级、底层的插件系统，可以介入Django的请求和响应处理过程，修改
Django的输入或输出。中间件的设计为开发者提供了一种无侵入式的开发方式，增强了Django框架的
健壮性，其它的MVC框架也有这个功能。

"""


# Django在中间件中预置了五个方法，这五个方法的区别在于不同的阶段执行，对输入或输出进行干预，
class MyMedd(MiddlewareMixin):
    # 在每个请求上，request对象产生之后，url匹配之前调用，返回None或HttpResponse对象
    def process_request(self, request):
        print('------request--------')

    # 在每个请求上，url匹配之后，视图函数调用之前调用，返回None或HttpResponse对象。
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        print('--------view------')

    # 视图函数调用之后，所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
    def process_response(self, request, response):
        print('-------response---')
        return response

    # 当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
    def process_exception(self, request, exception):
        pass
