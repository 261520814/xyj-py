# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class ChildrenCoupon(models.Model):
    user_id = models.PositiveIntegerField()
    code = models.CharField(max_length=20)
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    zid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'children_coupon'


class ChildrenUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    a1_money = models.DecimalField(max_digits=10, decimal_places=6)
    create_time = models.PositiveIntegerField()
    a1 = models.PositiveIntegerField()
    order_id = models.BigIntegerField()
    a2 = models.PositiveIntegerField()
    a3 = models.PositiveIntegerField()
    a2_zan = models.PositiveIntegerField()
    a2_complete_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'children_user'


class ChildrenZan(models.Model):
    id = models.BigAutoField(primary_key=True)
    openid = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'children_zan'


class ChildrenZhou(models.Model):
    zid = models.AutoField(primary_key=True)
    zname = models.CharField(max_length=255, blank=True, null=True)
    zimg = models.CharField(max_length=255, blank=True, null=True)
    zexp = models.CharField(max_length=255, blank=True, null=True)
    starttime = models.CharField(max_length=255, blank=True, null=True)
    endtime = models.CharField(max_length=255, blank=True, null=True)
    ztime = models.CharField(max_length=255, blank=True, null=True)
    zktime = models.CharField(max_length=255, blank=True, null=True)
    zcode = models.CharField(max_length=255, blank=True, null=True)
    zstatus = models.IntegerField(blank=True, null=True)
    starttimes = models.CharField(max_length=255, blank=True, null=True)
    endtimes = models.CharField(max_length=255, blank=True, null=True)
    fxbt = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'children_zhou'


class JdArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    areaid = models.CharField(db_column='areaId', unique=True, max_length=10, blank=True, null=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='areaName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    parentid = models.CharField(db_column='parentId', max_length=10, blank=True, null=True)  # Field name made lowercase.
    arealevel = models.IntegerField(db_column='areaLevel', blank=True, null=True)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='logTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'jd_area'



class MUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    create_time = models.IntegerField()
    zan = models.BigIntegerField()
    is_kai = models.PositiveIntegerField()
    is_zan = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'm_user'


class MZan(models.Model):
    id = models.BigAutoField(primary_key=True)
    openid = models.CharField(max_length=255)
    user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'm_zan'


class XinGiftOne(models.Model):
    user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xin_gift_one'


class XinGiftPlat(models.Model):
    user_id = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    plat_id = models.PositiveIntegerField()
    gift_name = models.CharField(max_length=255)
    gift_money = models.DecimalField(max_digits=10, decimal_places=2)
    gift_img = models.CharField(max_length=200)
    img = models.CharField(max_length=255)
    code = models.BigIntegerField()
    state = models.PositiveIntegerField()
    post_name = models.CharField(max_length=100, blank=True, null=True)
    post_number = models.CharField(max_length=200, blank=True, null=True)
    postinfo = models.TextField(db_column='postInfo', blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xin_gift_plat'


class XinGiftTwo(models.Model):
    tel = models.CharField(max_length=11)
    orderid = models.CharField(db_column='orderId', max_length=60)  # Field name made lowercase.
    exchangecode = models.CharField(db_column='exchangeCode', max_length=100)  # Field name made lowercase.
    codevalidity = models.DateField(db_column='codeValidity')  # Field name made lowercase.
    wnorderid = models.CharField(db_column='wnOrderId', max_length=100)  # Field name made lowercase.
    create_time = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xin_gift_two'


class XysAddress(models.Model):
    id = models.BigIntegerField(primary_key=True)
    uid = models.BigIntegerField()
    province = models.CharField(max_length=60)
    city = models.CharField(max_length=60)
    address = models.CharField(max_length=100)
    tel = models.CharField(max_length=20)
    name = models.CharField(max_length=60)
    create_time = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xys_address'


class XysAdmin(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=255)
    uname = models.CharField(max_length=255)
    upwd = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    create_ip = models.CharField(max_length=100)
    login_time = models.PositiveIntegerField()
    login_ip = models.CharField(max_length=100)
    level = models.PositiveIntegerField()
    isno = models.PositiveIntegerField()
    plat_id = models.PositiveIntegerField()

    def __str__(self):
        return self.uname

    class Meta:
        managed = False
        db_table = 'xys_admin'

    def to_dict(self):
        dict = {}
        dict['id'] = self.id
        dict['phone'] = self.phone
        dict['uname'] = self.uname
        dict['upwd'] = self.upwd
        dict['create_time'] = self.create_time
        dict['login_time'] = self.login_time
        dict['create_ip'] = self.create_ip
        dict['login_ip'] = self.login_ip
        dict['create_ip'] = self.create_ip
        dict['level'] = self.level
        dict['isno'] = self.isno
        dict['plat_id'] = self.plat_id
        return dict


class XysAdminIp(models.Model):
    id = models.BigAutoField(primary_key=True)
    ip = models.CharField(max_length=20)
    name = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'xys_admin_ip'


class XysAlertTime(models.Model):
    user_id = models.IntegerField(blank=True, null=True)
    alert_time = models.DateField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_alert_time'


class XysAssistant(models.Model):
    name = models.CharField(max_length=255)
    answer = models.TextField()
    sort = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    pid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_assistant'


class XysAward(models.Model):
    type = models.PositiveIntegerField()
    shop_id = models.PositiveIntegerField()
    num = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    ditch_id = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    order_id = models.PositiveIntegerField()
    pull_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_award'


class XysBaseLog(models.Model):
    user_id = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    page = models.PositiveIntegerField()
    content = models.TextField()
    sou = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_base_log'


class XysBranch(models.Model):
    fname = models.CharField(max_length=255)
    zname = models.CharField(max_length=255)
    hid = models.CharField(max_length=255)
    bname = models.CharField(max_length=255)
    bpwd = models.CharField(max_length=255)
    tel = models.CharField(max_length=100)
    create_time = models.PositiveIntegerField()
    login_time = models.PositiveIntegerField()
    login_ip = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    cid = models.BigIntegerField()
    linkman = models.CharField(max_length=255)
    linkman_tel = models.CharField(max_length=100)
    remark = models.CharField(max_length=255)
    is_jh = models.PositiveIntegerField()
    is_channel = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_branch'


class XysBranchcity(models.Model):
    id = models.BigAutoField(primary_key=True)
    cityname = models.CharField(max_length=100)
    create_time = models.PositiveIntegerField()
    upid = models.BigIntegerField()
    is_make = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_branchcity'


class XysBtnLog(models.Model):
    user_id = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    page = models.PositiveIntegerField()
    content = models.TextField()
    sou = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_btn_log'


class XysBusLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    openid = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    lb = models.DecimalField(max_digits=10, decimal_places=2)
    is_kai = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_bus_log'


class XysChannel(models.Model):
    platform_id = models.PositiveIntegerField()
    branch_id = models.PositiveIntegerField()
    channel = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    checkorganizationno = models.CharField(db_column='CheckOrganizationNo', max_length=40, blank=True, null=True)  # Field name made lowercase.
    accountmaneagerno = models.CharField(db_column='AccountManeagerNo', max_length=40, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xys_channel'


class XysChunk(models.Model):
    name = models.CharField(max_length=60)
    sort = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'xys_chunk'


class XysDouble(models.Model):
    user_id = models.BigIntegerField()
    double = models.DecimalField(max_digits=4, decimal_places=1)
    create_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    date = models.DateField()
    openid = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'xys_double'


class XysJdLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    jdorderid = models.CharField(db_column='jdOrderId', max_length=100)  # Field name made lowercase.
    thirdorder = models.CharField(db_column='thirdOrder', max_length=60)  # Field name made lowercase.
    sku = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    goodsfreight = models.DecimalField(db_column='goodsFreight', max_digits=10, decimal_places=2)  # Field name made lowercase.
    code = models.CharField(max_length=20)
    msg = models.CharField(max_length=200)
    postinfo = models.TextField(db_column='postInfo')  # Field name made lowercase.
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    user_id = models.PositiveIntegerField()
    orderids = models.CharField(db_column='orderIds', max_length=250)  # Field name made lowercase.
    is_now = models.PositiveIntegerField()
    is_new = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_jd_log'


class XysLbLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    lb = models.CharField(max_length=60)
    create_time = models.PositiveIntegerField()
    explain = models.CharField(db_column='Explain', max_length=255)  # Field name made lowercase.
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_lb_log'


class XysLoginLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.BigIntegerField()
    openid = models.CharField(max_length=255)
    login_time = models.PositiveIntegerField()
    time = models.DecimalField(max_digits=10, decimal_places=2)
    url = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_login_log'


class XysMcPlatform(models.Model):
    name = models.CharField(max_length=255)
    linkman = models.CharField(max_length=40)
    tel = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    code = models.CharField(max_length=255)
    xy_id = models.CharField(max_length=100, blank=True, null=True)
    banner = models.CharField(max_length=200, blank=True, null=True)
    logo = models.CharField(max_length=200, blank=True, null=True)
    address_json = models.TextField(blank=True, null=True)
    gift_name = models.CharField(max_length=255, blank=True, null=True)
    gift_img = models.CharField(max_length=200, blank=True, null=True)
    gift_money = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    gift_banner = models.CharField(max_length=200, blank=True, null=True)
    notice = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_mc_platform'


class XysMcStaff(models.Model):
    name = models.CharField(max_length=60)
    number = models.CharField(max_length=40)
    plat_id = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    tel = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'xys_mc_staff'


class XysMcSweep(models.Model):
    orderlogid = models.PositiveIntegerField(db_column='orderLogId', blank=True, null=True)  # Field name made lowercase.
    state = models.PositiveIntegerField(blank=True, null=True)
    msg = models.CharField(max_length=255, blank=True, null=True)
    type = models.PositiveIntegerField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    tel = models.CharField(max_length=20, blank=True, null=True)
    jurisdiction = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField(blank=True, null=True)
    remark = models.CharField(max_length=255)
    shopname = models.CharField(max_length=255, blank=True, null=True)
    shopimg = models.CharField(max_length=255, blank=True, null=True)
    money = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    is_xrl = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_mc_sweep'


class XysMdCount(models.Model):
    openid = models.CharField(max_length=50)
    type = models.CharField(max_length=255)
    count = models.IntegerField()
    ip = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_md_count'


class XysMdbase(models.Model):
    date = models.PositiveIntegerField()
    dayisit1 = models.PositiveIntegerField()
    dayisit2 = models.PositiveIntegerField()
    dayreg1 = models.PositiveIntegerField()
    dayreg2 = models.PositiveIntegerField()
    daysign1 = models.PositiveIntegerField()
    daysign2 = models.PositiveIntegerField()
    daysignmoney1 = models.PositiveIntegerField()
    daysignmoney2 = models.PositiveIntegerField()
    daydelmoney1 = models.PositiveIntegerField()
    daydelmoney2 = models.PositiveIntegerField()
    dayhomeuv1 = models.PositiveIntegerField()
    dayhomeuv2 = models.PositiveIntegerField()
    dayxrluv1 = models.PositiveIntegerField()
    dayxrluv2 = models.PositiveIntegerField()
    dayxrlno1 = models.PositiveIntegerField()
    dayxrlno2 = models.PositiveIntegerField()
    dayxrlgo1 = models.PositiveIntegerField()
    dayxrlgo2 = models.PositiveIntegerField()
    daydetail1 = models.PositiveIntegerField()
    daydetail2 = models.PositiveIntegerField()
    daybtn1 = models.PositiveIntegerField()
    daybtn2 = models.PositiveIntegerField()
    daylogin1 = models.PositiveIntegerField()
    daylogin2 = models.PositiveIntegerField()
    dayths1 = models.PositiveIntegerField()
    dayths2 = models.PositiveIntegerField()
    dayths3 = models.PositiveIntegerField()
    shop1 = models.PositiveIntegerField()
    shop2 = models.PositiveIntegerField()
    shop3 = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_mdbase'


class XysMutualLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    get_user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    lb = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'xys_mutual_log'


class XysNews(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    type = models.PositiveIntegerField()
    is_index = models.PositiveIntegerField()
    url = models.CharField(max_length=200, blank=True, null=True)
    sort = models.PositiveIntegerField()
    img = models.CharField(max_length=255, blank=True, null=True)
    url_type = models.CharField(max_length=100)
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_news'


class XysOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.BigIntegerField()
    shop_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    gettype = models.BigIntegerField()
    uname = models.CharField(max_length=100)
    utel = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    gettime = models.PositiveIntegerField()
    relation = models.CharField(max_length=100)
    lb = models.DecimalField(max_digits=10, decimal_places=1)
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    post_number = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    post_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    get_cid = models.BigIntegerField()
    count = models.PositiveIntegerField()
    is_prize = models.IntegerField()
    type = models.PositiveIntegerField()
    is_sec = models.PositiveIntegerField()
    sec_id = models.PositiveIntegerField()
    wm_code = models.CharField(max_length=200)
    zt_content = models.TextField(blank=True, null=True)
    shop_type = models.PositiveIntegerField()
    wnorderid = models.CharField(db_column='wnOrderId', max_length=100)  # Field name made lowercase.
    wninfo = models.TextField(db_column='wnInfo')  # Field name made lowercase.
    url_type = models.PositiveIntegerField()
    is_sms = models.PositiveIntegerField()
    is_jd = models.PositiveIntegerField()
    award_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_order'


class XysPageLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    page = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    isnew = models.PositiveIntegerField()
    openid = models.CharField(max_length=100)
    url = models.PositiveIntegerField()
    gid = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_page_log'


class XysPrize(models.Model):
    name = models.CharField(max_length=55)
    picurl = models.CharField(max_length=255)
    picurl_big = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    send_num = models.IntegerField()
    surplus_num = models.IntegerField()
    probability = models.IntegerField()
    sponsor = models.CharField(max_length=155)
    sponsor_mobile = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    send_type = models.CharField(max_length=2)
    sort = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xys_prize'


class XysPrizeConfig(models.Model):
    id = models.IntegerField(primary_key=True)
    prize_start_time = models.IntegerField(blank=True, null=True)
    prize_end_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_prize_config'


class XysPrizeCopy(models.Model):
    name = models.CharField(max_length=55)
    picurl = models.CharField(max_length=255)
    picurl_big = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    send_num = models.IntegerField()
    surplus_num = models.IntegerField()
    probability = models.IntegerField()
    sponsor = models.CharField(max_length=155)
    sponsor_mobile = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    send_type = models.CharField(max_length=2)
    status = models.IntegerField()
    sort = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xys_prize_copy'


class XysSaveLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    phone = models.CharField(max_length=11)
    openid = models.CharField(max_length=100)
    create_time = models.PositiveIntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_save_log'


class XysShareLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    uid = models.BigIntegerField()
    openid = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    type = models.CharField(max_length=30)
    urlc = models.CharField(max_length=255)
    hid = models.BigIntegerField()
    page = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_share_log'


class XysShop(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    describe = models.TextField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    lb = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    protect = models.PositiveIntegerField()
    gettype = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    is_new = models.PositiveIntegerField()
    tid = models.BigIntegerField()
    rule = models.CharField(max_length=255)
    img_logo = models.CharField(max_length=255)
    branch_id = models.CharField(max_length=255)
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    sec_lb = models.DecimalField(max_digits=10, decimal_places=2)
    is_sec = models.PositiveIntegerField()
    sec_stock = models.PositiveIntegerField()
    code = models.TextField()
    cardbatchno = models.CharField(db_column='cardBatchNo', max_length=200)  # Field name made lowercase.
    goodscode = models.CharField(db_column='goodsCode', max_length=40)  # Field name made lowercase.
    jd_money = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'xys_shop'


class XysShopCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.BigIntegerField()
    code = models.CharField(max_length=60)
    user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    order_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_shop_code'


class XysShopCopy1(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    describe = models.TextField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    lb = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    protect = models.PositiveIntegerField()
    gettype = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    is_new = models.PositiveIntegerField()
    tid = models.BigIntegerField()
    rule = models.CharField(max_length=255)
    img_logo = models.CharField(max_length=255)
    branch_id = models.CharField(max_length=255)
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    sec_lb = models.DecimalField(max_digits=10, decimal_places=2)
    is_sec = models.PositiveIntegerField()
    sec_stock = models.PositiveIntegerField()
    code = models.TextField()
    cardbatchno = models.CharField(db_column='cardBatchNo', max_length=200)  # Field name made lowercase.
    goodscode = models.CharField(db_column='goodsCode', max_length=40)  # Field name made lowercase.
    jd_money = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'xys_shop_copy1'


class XysShopKdf(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    complete_time = models.PositiveIntegerField()
    shop_id = models.BigIntegerField()
    user_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_shop_kdf'


class XysShopSec(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.PositiveIntegerField()
    start_time = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    sec_lb = models.DecimalField(max_digits=10, decimal_places=2)
    sec_sum = models.PositiveIntegerField()
    sec_stock = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_shop_sec'


class XysShopStock(models.Model):
    branch_id = models.PositiveIntegerField()
    shop_id = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_shop_stock'


class XysSmsLog(models.Model):
    tel = models.CharField(max_length=11)
    type = models.PositiveIntegerField()
    create_time = models.IntegerField()
    complete_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_sms_log'


class XysSystem(models.Model):
    wish_n_day = models.PositiveIntegerField()
    y_rate = models.DecimalField(max_digits=10, decimal_places=4)
    n_lb = models.DecimalField(max_digits=5, decimal_places=2)
    bus_count = models.PositiveIntegerField()
    bus_kaihu = models.PositiveIntegerField()
    bus_max = models.PositiveIntegerField()
    mutual_max = models.PositiveIntegerField()
    day_lb = models.PositiveIntegerField()
    userinfo_log = models.BigIntegerField()
    xyinfo = models.CharField(max_length=255)
    zan_log = models.BigIntegerField()
    page_log = models.BigIntegerField()
    maxamount = models.PositiveIntegerField(db_column='maxAmount')  # Field name made lowercase.
    post_tel = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'xys_system'


class XysTest(models.Model):
    uid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    time = models.CharField(max_length=255, blank=True, null=True)
    zid = models.IntegerField(blank=True, null=True)
    openid = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    hid = models.CharField(max_length=255, blank=True, null=True)
    hname = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_test'


class XysTtttt(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=11, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_ttttt'


class XysUser(models.Model):
    uid = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=11)
    create_time = models.PositiveIntegerField()
    openid = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    headimgurl = models.CharField(max_length=255)
    province = models.CharField(max_length=255)
    state = models.PositiveIntegerField()
    fenhang = models.CharField(max_length=255)
    zhihang = models.CharField(max_length=255)
    hid = models.BigIntegerField()
    isnew = models.PositiveIntegerField()
    isopenbank = models.PositiveIntegerField()
    sex = models.PositiveIntegerField()
    share = models.BigIntegerField()
    type = models.PositiveIntegerField()
    login_time = models.PositiveIntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    lb = models.DecimalField(max_digits=16, decimal_places=6)
    is_index = models.PositiveIntegerField()
    open_state = models.PositiveIntegerField()
    is_card = models.PositiveIntegerField()
    promcode = models.CharField(db_column='PromCode', max_length=100)  # Field name made lowercase.
    is_mother = models.PositiveIntegerField()
    is_sc = models.IntegerField()
    start_time = models.PositiveIntegerField()
    is_children = models.IntegerField()
    is_year = models.PositiveIntegerField()
    money_ky = models.DecimalField(max_digits=10, decimal_places=2)
    head_path = models.CharField(max_length=160)
    xin_uid = models.BigIntegerField()
    is_my = models.IntegerField()
    share_code = models.CharField(max_length=160)
    is_xyj = models.IntegerField()
    ditch_id = models.PositiveIntegerField()
    is_huafei = models.PositiveIntegerField()
    channel = models.PositiveIntegerField()
    votes = models.PositiveIntegerField()
    is_vote = models.PositiveIntegerField()
    havetel = models.CharField(db_column='haveTel', max_length=11)  # Field name made lowercase.
    sou = models.PositiveIntegerField()
    username = models.CharField(max_length=20)
    plat_id = models.PositiveIntegerField()
    staff_id = models.PositiveIntegerField()
    is_wallet = models.PositiveIntegerField()
    workerid = models.CharField(db_column='WorkerId', max_length=30)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'xys_user'


class XysUserInfo(models.Model):
    jid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=32, blank=True, null=True)
    user_no = models.CharField(max_length=20, blank=True, null=True)
    global_id = models.CharField(max_length=32, blank=True, null=True)
    client_name = models.CharField(max_length=32, blank=True, null=True)
    client_no = models.CharField(max_length=32, blank=True, null=True)
    card_num = models.CharField(max_length=32, blank=True, null=True)
    card_num2 = models.CharField(max_length=32, blank=True, null=True)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    channel_id = models.CharField(max_length=32, blank=True, null=True)
    manager_id = models.CharField(max_length=32, blank=True, null=True)
    identify_code = models.CharField(max_length=256, blank=True, null=True)
    create_date = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.CharField(max_length=32, blank=True, null=True)
    update_date = models.CharField(max_length=32, blank=True, null=True)
    update_time = models.CharField(max_length=32, blank=True, null=True)
    host_user_no = models.CharField(max_length=32, blank=True, null=True)
    mrch_no = models.CharField(max_length=64, blank=True, null=True)
    appid = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_user_info'


class XysUserInfoCopy1(models.Model):
    jid = models.AutoField(primary_key=True)
    id = models.CharField(max_length=32, blank=True, null=True)
    user_no = models.CharField(max_length=20, blank=True, null=True)
    global_id = models.CharField(max_length=32, blank=True, null=True)
    client_name = models.CharField(max_length=32, blank=True, null=True)
    client_no = models.CharField(max_length=32, blank=True, null=True)
    card_num = models.CharField(max_length=32, blank=True, null=True)
    card_num2 = models.CharField(max_length=32, blank=True, null=True)
    mobile = models.CharField(max_length=32, blank=True, null=True)
    channel_id = models.CharField(max_length=32, blank=True, null=True)
    manager_id = models.CharField(max_length=32, blank=True, null=True)
    identify_code = models.CharField(max_length=256, blank=True, null=True)
    create_date = models.CharField(max_length=32, blank=True, null=True)
    create_time = models.CharField(max_length=32, blank=True, null=True)
    update_date = models.CharField(max_length=32, blank=True, null=True)
    update_time = models.CharField(max_length=32, blank=True, null=True)
    host_user_no = models.CharField(max_length=32, blank=True, null=True)
    mrch_no = models.CharField(max_length=64, blank=True, null=True)
    appid = models.CharField(max_length=64, blank=True, null=True)
    user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_user_info_copy1'


class XysWalletDitch(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    upper = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    sole = models.CharField(max_length=60, blank=True, null=True)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    type = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_wallet_ditch'


class XysWish(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=10, decimal_places=1)
    lb = models.DecimalField(max_digits=10, decimal_places=1)
    remarks = models.TextField()
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    del_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_wish'


class XysWishOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.BigIntegerField()
    wish_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    intype = models.BigIntegerField()
    uname = models.CharField(max_length=100)
    utel = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    lb = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    target_time = models.PositiveIntegerField()
    money = models.DecimalField(max_digits=10, decimal_places=2)
    over = models.PositiveIntegerField()
    plan = models.PositiveIntegerField()
    remark = models.CharField(max_length=255)
    day = models.PositiveIntegerField()
    money_a = models.DecimalField(max_digits=10, decimal_places=2)
    post_name = models.CharField(max_length=255)
    post_number = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    next_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_wish_order'


class XysXinOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    number = models.BigIntegerField()
    shop_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    uname = models.CharField(max_length=100)
    utel = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    money_ck = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    target_time = models.PositiveIntegerField()
    shop_type = models.PositiveIntegerField()
    remark = models.CharField(max_length=255)
    post_name = models.CharField(max_length=255)
    post_number = models.CharField(max_length=255)
    next_time = models.PositiveIntegerField()
    gettype = models.IntegerField()
    relation = models.CharField(max_length=20)
    acctno = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)
    del_time = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    is_prize = models.IntegerField()
    url_type = models.PositiveIntegerField()
    is_continue = models.PositiveIntegerField()
    year_hf = models.PositiveIntegerField()
    plat_id = models.PositiveIntegerField()
    end_time = models.PositiveIntegerField()
    is_now = models.PositiveIntegerField()
    beizhu = models.CharField(max_length=300)
    award_id = models.PositiveIntegerField()
    card = models.CharField(max_length=40, blank=True, null=True)
    channel = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xys_xin_order'


class XysXinOrderCancel(models.Model):
    id = models.BigAutoField(primary_key=True)
    ditchid = models.PositiveIntegerField(db_column='ditchId')  # Field name made lowercase.
    plat_id = models.PositiveIntegerField()
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    acctno = models.CharField(max_length=100)
    money_ck = models.DecimalField(max_digits=10, decimal_places=2)
    target_time = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_xin_order_cancel'


class XysXinOrderLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    order_id = models.BigIntegerField()
    user_id = models.BigIntegerField()
    shop_id = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    state = models.PositiveIntegerField()
    target_time = models.PositiveIntegerField()
    shop_type = models.PositiveIntegerField()
    remark = models.CharField(max_length=255)
    date = models.CharField(max_length=60)
    post_name = models.CharField(max_length=100)
    post_number = models.CharField(max_length=60)
    post_time = models.PositiveIntegerField()
    qi = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    week = models.PositiveIntegerField()
    postinfo = models.TextField(db_column='postInfo')  # Field name made lowercase.
    goodscode = models.CharField(db_column='goodsCode', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    number = models.CharField(max_length=40, blank=True, null=True)
    plat_id = models.PositiveIntegerField()
    code = models.BigIntegerField(blank=True, null=True)
    is_jd = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_xin_order_log'


class XysXinShop(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    money_ck = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    protect = models.PositiveIntegerField()
    protecttype = models.PositiveIntegerField(db_column='protectType')  # Field name made lowercase.
    way = models.PositiveIntegerField()
    waytype = models.PositiveIntegerField(db_column='wayType')  # Field name made lowercase.
    count = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    rule = models.TextField()
    branch_id = models.CharField(max_length=255)
    type = models.IntegerField()
    unit = models.CharField(max_length=60)
    is_index = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    cardbatchno = models.PositiveIntegerField(db_column='cardBatchNo')  # Field name made lowercase.
    is_coupon = models.PositiveIntegerField()
    sign_day = models.PositiveIntegerField()
    sign_count = models.PositiveIntegerField()
    sign_address = models.CharField(max_length=100)
    sign_name = models.CharField(max_length=100)
    sign_tel = models.CharField(max_length=60)
    sign_date = models.DateField(blank=True, null=True)
    goodscode = models.CharField(db_column='goodsCode', max_length=200)  # Field name made lowercase.
    jd_money = models.DecimalField(max_digits=10, decimal_places=2)
    shop_type = models.PositiveIntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    goodscode2 = models.CharField(db_column='goodsCode2', max_length=200)  # Field name made lowercase.
    jd_money2 = models.DecimalField(max_digits=10, decimal_places=2)
    goodscode3 = models.CharField(db_column='goodsCode3', max_length=200)  # Field name made lowercase.
    jd_money3 = models.DecimalField(max_digits=10, decimal_places=2)
    xygz = models.TextField(blank=True, null=True)
    plat_id = models.PositiveIntegerField()
    is_hot = models.PositiveIntegerField()
    is_only = models.PositiveIntegerField()
    zuhe = models.PositiveIntegerField()
    group = models.CharField(max_length=255)
    ditch_ids = models.CharField(max_length=200)
    period_start = models.PositiveIntegerField()
    period_end = models.PositiveIntegerField()
    is_now = models.PositiveIntegerField()
    visits = models.BigIntegerField()
    is_gift = models.PositiveIntegerField()
    chunk_ids = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'xys_xin_shop'


class XysXinShopCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    shop_id = models.BigIntegerField()
    code = models.CharField(max_length=60)
    user_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()
    complete_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    order_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_xin_shop_code'


class XysXinShopCopy(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    money_ck = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    protect = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    rule = models.TextField()
    branch_id = models.CharField(max_length=255)
    type = models.IntegerField()
    unit = models.CharField(max_length=60)
    is_index = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    cardbatchno = models.PositiveIntegerField(db_column='cardBatchNo')  # Field name made lowercase.
    is_coupon = models.PositiveIntegerField()
    sign_day = models.PositiveIntegerField()
    sign_count = models.PositiveIntegerField()
    sign_address = models.CharField(max_length=100)
    sign_name = models.CharField(max_length=100)
    sign_tel = models.CharField(max_length=60)
    sign_date = models.DateField(blank=True, null=True)
    goodscode = models.CharField(db_column='goodsCode', max_length=200)  # Field name made lowercase.
    jd_money = models.DecimalField(max_digits=10, decimal_places=2)
    shop_type = models.PositiveIntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    goodscode2 = models.CharField(db_column='goodsCode2', max_length=200)  # Field name made lowercase.
    jd_money2 = models.DecimalField(max_digits=10, decimal_places=2)
    goodscode3 = models.CharField(db_column='goodsCode3', max_length=200)  # Field name made lowercase.
    jd_money3 = models.DecimalField(max_digits=10, decimal_places=2)
    xygz = models.TextField(blank=True, null=True)
    plat_id = models.PositiveIntegerField()
    is_hot = models.PositiveIntegerField()
    is_only = models.PositiveIntegerField()
    zuhe = models.PositiveIntegerField()
    group = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'xys_xin_shop_copy'


class XysXinShopCopy1(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    describe = models.CharField(max_length=255)
    money = models.DecimalField(max_digits=10, decimal_places=2)
    money_ck = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    protect = models.PositiveIntegerField()
    protecttype = models.PositiveIntegerField(db_column='protectType')  # Field name made lowercase.
    way = models.PositiveIntegerField()
    waytype = models.PositiveIntegerField(db_column='wayType')  # Field name made lowercase.
    count = models.PositiveIntegerField()
    img = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    rule = models.TextField()
    branch_id = models.CharField(max_length=255)
    type = models.IntegerField()
    unit = models.CharField(max_length=60)
    is_index = models.PositiveIntegerField()
    sort = models.PositiveIntegerField()
    cardbatchno = models.PositiveIntegerField(db_column='cardBatchNo')  # Field name made lowercase.
    is_coupon = models.PositiveIntegerField()
    sign_day = models.PositiveIntegerField()
    sign_count = models.PositiveIntegerField()
    sign_address = models.CharField(max_length=100)
    sign_name = models.CharField(max_length=100)
    sign_tel = models.CharField(max_length=60)
    sign_date = models.DateField(blank=True, null=True)
    goodscode = models.CharField(db_column='goodsCode', max_length=200)  # Field name made lowercase.
    jd_money = models.DecimalField(max_digits=10, decimal_places=2)
    shop_type = models.PositiveIntegerField()
    label = models.CharField(max_length=255, blank=True, null=True)
    goodscode2 = models.CharField(db_column='goodsCode2', max_length=200)  # Field name made lowercase.
    jd_money2 = models.DecimalField(max_digits=10, decimal_places=2)
    goodscode3 = models.CharField(db_column='goodsCode3', max_length=200)  # Field name made lowercase.
    jd_money3 = models.DecimalField(max_digits=10, decimal_places=2)
    xygz = models.TextField(blank=True, null=True)
    plat_id = models.PositiveIntegerField()
    is_hot = models.PositiveIntegerField()
    is_only = models.PositiveIntegerField()
    zuhe = models.PositiveIntegerField()
    group = models.CharField(max_length=255)
    ditch_ids = models.CharField(max_length=200)
    period_start = models.PositiveIntegerField()
    period_end = models.PositiveIntegerField()
    is_now = models.PositiveIntegerField()
    visits = models.BigIntegerField()
    is_gift = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_xin_shop_copy1'


class XysXinShopStock(models.Model):
    branch_id = models.PositiveIntegerField()
    shop_id = models.PositiveIntegerField()
    stock = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_xin_shop_stock'


class XysXinStaff(models.Model):
    uid = models.IntegerField()
    realname = models.CharField(max_length=55)
    mobile = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    company = models.CharField(max_length=55)
    comp_address = models.CharField(max_length=255)
    content = models.TextField()
    create_time = models.IntegerField()
    status = models.IntegerField()
    vote_num = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xys_xin_staff'


class XysYearPrize(models.Model):
    name = models.CharField(max_length=55)
    picurl = models.CharField(max_length=255)
    picurl_big = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    send_num = models.IntegerField()
    surplus_num = models.IntegerField()
    probability = models.IntegerField()
    sponsor = models.CharField(max_length=155)
    sponsor_mobile = models.CharField(max_length=25)
    description = models.CharField(max_length=255)
    send_type = models.CharField(max_length=2)
    sort = models.IntegerField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'xys_year_prize'


class XysYearTel(models.Model):
    tel = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'xys_year_tel'


class XysYearUnity(models.Model):
    user_id = models.PositiveIntegerField()
    user_id1 = models.PositiveIntegerField()
    user_id2 = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    in_time1 = models.IntegerField()
    in_time2 = models.PositiveIntegerField()
    prize_id = models.PositiveIntegerField()
    old_num = models.PositiveIntegerField()
    man_user_id = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_year_unity'


class XysYearly(models.Model):
    fest = models.CharField(max_length=40, blank=True, null=True)
    goods = models.CharField(max_length=100, blank=True, null=True)
    update_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_yearly'


class XysYhLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField()
    openid = models.CharField(max_length=160)
    lb = models.BigIntegerField()
    number = models.CharField(max_length=100)
    shop_id = models.BigIntegerField()
    create_time = models.PositiveIntegerField()
    del_time = models.IntegerField()
    phone = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'xys_yh_log'


class XysZtBranch(models.Model):
    zname = models.CharField(max_length=55)
    tel = models.CharField(max_length=25)
    address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'xys_zt_branch'


class XysZzVote(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    detail = models.TextField()
    img = models.CharField(max_length=200)
    votes = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()
    del_time = models.PositiveIntegerField()
    tel = models.CharField(max_length=11)
    company = models.CharField(max_length=60)
    sort = models.PositiveIntegerField()
    source = models.CharField(max_length=100)
    headimg = models.CharField(max_length=200)
    tp_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_zz_vote'


class XysZzVotesGetLog(models.Model):
    user_id = models.PositiveIntegerField()
    type = models.IntegerField()
    num = models.PositiveIntegerField()
    craete_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_zz_votes_get_log'


class XysZzVotesLog(models.Model):
    zz_id = models.PositiveIntegerField()
    uid = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'xys_zz_votes_log'


class ZtqcCoupon(models.Model):
    uid = models.PositiveIntegerField()
    create_time = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'ztqc_coupon'
