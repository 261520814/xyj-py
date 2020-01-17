import json
import re
import time

import requests
from bs4 import BeautifulSoup
from django.db.models import Q
from django.shortcuts import render

from adm.models.ditch import Ditch
from adm.models.models import XysXinShop, XysChunk, XysWalletDitch
from adm.views.func import get, suc, post, params, err, getSqlObj, getPage, download


@get
def list(request):
    # 请求头部
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    # url = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0'
    # url2= 'https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=time&page_limit=20&page_start=0'
    # res = requests.get(url, headers=headers)
    # if res.status_code != 200:
    #     return err(res.status_code)
    # obj = json.loads(res.text)
    # dict = {}
    # list = []
    # return suc(obj['subjects'])
    # for item in obj['subjects']:
    #
    #     dict = {"name": item['title'], }
    #     list.append({"name": item['title']})
    #
    #
    # return suc(list)




    # 获取请求页码，没有就是第一页
    page = request.GET.get("page", 1)

    # 获取查询时间范围，没有就给默认
    start = "1970-12-31" if request.GET.get("start", "1970-12-31") == '' else request.GET.get("start", "1970-12-31")
    end = "2099-12-31" if request.GET.get("end", "2099-12-31") == '' else request.GET.get("end", "2099-12-31")

    # 日期转时间戳
    timeStart = int(time.mktime(time.strptime(start, "%Y-%m-%d")))
    timeEnd = int(time.mktime(time.strptime(end, "%Y-%m-%d")))

    # 根据条件查询模型对象
    lists = XysXinShop.objects.filter(del_time__lte=1, create_time__gte=timeStart, create_time__lt=timeEnd).values("id", "chunk_ids", "img", "name", "shop_type", "money", "money_ck", "protect", "protecttype", "way", "waytype", "del_time").order_by("-id")

    # 关键字搜索加上模糊查询条件
    if request.GET.get("name", None):
        lists = lists.filter(name__contains=request.GET.get("name"))

    # 如果选择了商品类型，加上类型条件
    if request.GET.get("shopType", None):
        lists = lists.filter(shop_type=request.GET.get("shopType"))

    # 筛选凭条加上平台查询条件
    if request.GET.get("ditch", None):
        ditch_ids = request.GET.get("ditch").split("-")
        q = Q()
        for item in ditch_ids:
            q.add(Q(**{'ditch_ids__contains': '-'+item+'-'}), Q.OR)
            lists = lists.filter(q)
        # lists = lists.extra(where=['ditch_ids IN (' + request.GET.get("ditch") + ')'])
    # 分页，每页10条数据
    data, paginator = getPage(lists, page)

    # 所有板块
    chunk = XysChunk.objects.filter(del_time=0).values("id", "name")
    chunk_arr = {}
    for item in chunk:
        chunk_arr[item['id']] = item['name']

    # 商品所属板块拼接
    for item in data:
        item['chunk_name'] = ''
        Array = item['chunk_ids'].strip("-").split("-")
        for vo in Array:
            item['chunk_name'] += '[' + chunk_arr[int(vo)] + ']'

    # 平台查询
    ditchData = XysWalletDitch.objects.filter(del_time=0).values("id", "name")

    # 选中平台
    for item in ditchData:
        if "ditch_ids" in dir():
            item['checked'] = True if str(item['id']) in ditch_ids else False
        else:
            item['checked'] = True
    # 返回数据给模板
    return render(request, 'adm/goods/list.html', {"list": data, "paginator": paginator, "ditch": ditchData})

@get
def add(request):
    data = {}
    if not request.GET.get("id", None):
        # 没有id，新增
        pass
    else:
        # 有id，编辑
        id = request.GET.get("id")
        data['res'] = Ditch.objects.get(pk=id)
    return render(request, 'adm/ditch/add.html', data)

@post
@params("name", "sole", "upper", "type")
def add_c(request, args):
    if not request.POST.get("id", None):
        # 没有id，新增
        obj = getSqlObj(request.POST)
        res = Ditch.objects.create(** obj)
    else:
        # 有id，编辑
        res = Ditch.objects.get(pk=request.POST.get("id"))
        res.name = args[0]
        res.sole = args[1]
        res.upper = args[2]
        res.type = args[3]
        res.save()
    return suc(res.to_dict())

@post
@params("id", "type")
def del_c(request, args):
    if args[1] == 1:
        res = Ditch.objects.get(pk=args[0])
        res.del_time = int(time.time())
        res.save()
    else:
        try:
            Ditch.objects.extra(where=['id IN (' + args[0] + ')']).update(del_time=int(time.time()))
            # Ditch.objects.extra(where=['id IN (' + args[0] + ')']).delete()
        except:
            return err("ID不存在")
    return suc()
    # res = Ditch.objects.filter(id=args[0]).delete()
    # try:
    #     if res[0] == 1:
    #         return suc()
    #     return err("删除失败")
    # except:
    #     return err("删除失败")