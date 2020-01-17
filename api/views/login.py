from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from adm.views.func import err, suc, post, params, get, md5
from api.models.models import XysAdmin

@csrf_exempt
@post
@params("username", "password")
def login_c(request, args):
    if not XysAdmin.objects.filter(uname=args[0]).exists():
        return err("用户不存在")

    res = XysAdmin.objects.get(uname=args[0])

    if res.upwd != md5(args[1]):
        return err("密码错误")

    # 拼装用户信息存session
    request.session['admInfo'] = res.to_dict()

    return suc(res.to_dict(), '登录成功1')
