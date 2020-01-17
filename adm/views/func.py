import hashlib
import urllib

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse, HttpResponseRedirect

# 接口查询错误返回
def err(info="error", data={}):
    res = {'code': -2, 'msg': info, 'data': data}
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})

# 接口成功返回
def suc(data={}, info="success"):
    res = {'code': 1, 'msg': info, 'data': data}
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


# 拦截非get请求
def get(func):
    def in_fun(request):
        if request.method == 'GET':
            return func(request)
        else:
            return err('not get request')

    return in_fun

# 拦截非post请求
def post(func):
    def in_fun(request):
        if request.method == 'POST':
            return func(request)
        else:
            return err('not post request')

    return in_fun

# 参数检查
def params(*args):  # 接收传入的字段
    def check_params(func):
        def in_fun(request):
            p = []
            for val in args:  # 遍历客户端请求是否包含字段
                param = request.POST.get(val, 100)
                if param == 100:  # 若不包含则返回错误
                    return err('need param %s' % val)
                else:
                    p.append(param)  # 若包含则传入数组返回给被装饰的函数
            return func(request, p)

        return in_fun

    return check_params

# md5加密
def md5(s):
    m = hashlib.md5(s.encode('utf8'))
    return m.hexdigest()

# 判断后管是否登录
def getAdmInfo(request):
    if not request.session.get("admInfo", None):
        return False
    return request.session.get("admInfo")

# 获取请求对象去掉csrf
def getSqlObj(objs):
    obj = {}
    for key, value in objs.items():
        obj[key] = value

    try:
        del obj['csrfmiddlewaretoken']
    except:
        pass
    return obj

# 获取分页
def getPage(lists, page=1, limit=10):
    # 分页，每页10条数据
    paginator = Paginator(lists, limit)

    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # 如果请求的页数不是整数，返回第一页。
        data = paginator.page(1)
    except EmptyPage:
        # 如果请求的页数不在合法的页数范围内，返回结果的最后一页。
        data = paginator.page(paginator.num_pages)

    return data, paginator

# 请求
def download(url):
    if url is None:
        return None

    # 伪装成浏览器访问，直接访问的话csdn会拒绝
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {
        'User-Agent': user_agent,
        # 'Host': 'https://movie.douban.com',
    }
    # 构造请求
    req = urllib.request.Request(url, headers=headers)
    # 访问页面
    response = urllib.request.urlopen(req)
    if response.status != 200:
        return response.status
    # python3中urllib.read返回的是bytes对象，不是string,得把它转换成string对象，用bytes.decode方法
    return response.read().decode()