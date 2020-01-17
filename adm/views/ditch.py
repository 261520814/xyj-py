import time

from django.shortcuts import render

from adm.models.ditch import Ditch
from adm.views.func import get, suc, post, params, err, getSqlObj, getPage


@get
def list(request):
    # 获取请求页码，没有就是第一页
    page = request.GET.get("page", 1)

    # 获取查询时间范围，没有就给默认
    start = request.GET.get("start", "1970-12-31")
    end = request.GET.get("end", "2099-12-31")
    start = "1970-12-31" if start == '' else start
    end = "2099-12-31" if end == '' else end

    # 日期转时间戳
    timeStart = int(time.mktime(time.strptime(start, "%Y-%m-%d")))
    timeEnd = int(time.mktime(time.strptime(end, "%Y-%m-%d")))

    # 根据条件查询模型对象
    lists = Ditch.objects.filter(del_time=0, create_time__gte=timeStart, create_time__lt=timeEnd).values("id", "name", "sole", "upper", "create_time", "type").order_by(
        "-id")

    # 关键字搜索加上模糊查询条件
    if request.GET.get("name", None):
        lists = lists.filter(name__contains=request.GET.get("name"))

    # 分页，每页10条数据
    data, paginator = getPage(lists, page)

    # 返回数据给模板
    return render(request, 'adm/ditch/list.html', {"list": data, "paginator": paginator})

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