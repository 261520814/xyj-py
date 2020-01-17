import demjson
import json
from django.shortcuts import render

# Create your views here.
from adm.models.index import Admin, XinOrder
from adm.views.func import suc, err, post, params, md5, getAdmInfo
from django.http import JsonResponse, HttpResponseRedirect

def login(request):
    pass
    return render(request, 'adm/login.html')

@post
@params("name", "password")
def login_c(request, args):
    if not Admin.objects.filter(uname=args[0]).exists():
        return err("用户不存在")

    res = Admin.objects.get(uname=args[0])

    if res.upwd != md5(args[1]):
        return err("密码错误")

    # 拼装用户信息存session
    request.session['admInfo'] = res.to_dict()
    return suc([], '登录成功')

# 退出登录
def logout(request):
    if not request.session.get("admInfo", None):
        return HttpResponseRedirect('/adm')

    del request.session['admInfo']  # 删除session
    return HttpResponseRedirect('/adm')

def home(request):
    admInfo = getAdmInfo(request)
    if not admInfo: return HttpResponseRedirect('/adm')

    return render(request, 'adm/index.html')

def welcome(request):
    data = {}
    data['sign_count'] = XinOrder.objects.filter(state=1).all().count()


    return render(request, 'adm/welcome.html', data)