
import datetime
from django import template

register = template.Library()

#注册过滤器
@register.filter(name='timeToDate')
def timeToDate(timeStamp):
    dateArray = datetime.datetime.fromtimestamp(timeStamp)
    otherStyleTime = dateArray.strftime("%Y-%m-%d %H:%M:%S")
    return otherStyleTime

@register.filter(name='ditchType')
def ditchType(type):
    if type == 0:
        return "微信"
    elif type == 1:
        return "钱包"
    else:
        return "APP"

@register.filter(name="val_Is_val")
def val_Is_val(val1, val2):
    if not val1: val1 = 1
    if int(val1) == int(val2):
        return True
    elif int(val1) == int(val2):
        return True
    else:
        return False

@register.filter(name="getShopType")
def getShopType(val):
    # 0普通商品，1话费直冲，2劵码，3京东直购，4本地券码，5线下代金券，6鲜花
    switch = {
        0: "普通商品",
        1: "话费直冲",
        2: "微能劵码",
        3: "京东直购",
        4: "本地券码",
        5: "商超",
        6: "鲜花",
    }
    try:
        return switch[int(val)]
    except:
        return "没有此类型"

@register.filter(name="getProtect")
def getProtect(protectType, protect):
    if protectType == 0:
        return str(protect) + "个月"
    elif protectType == 1:
        return str(protect) + "天"
    else:
        dateArray = datetime.datetime.fromtimestamp(protect)
        return dateArray.strftime("%Y-%m-%d")

@register.filter(name="getWay")
def getWay(wayType, way):
    if wayType == 0:
        return str(way) + "个月"
    elif wayType == 1:
        return str(way) + "天"
    else:
        dateArray = datetime.datetime.fromtimestamp(way)
        return dateArray.strftime("%Y-%m-%d")

@register.filter(name="intVal")
def intVal(val):
    return int(val)