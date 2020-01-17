from django.db import models

# Create your models here.

# 后管信息表
class Admin(models.Model):

    # gender = (
    #     ('male', "男"),
    #     ('female', "女"),
    # )

    phone = models.CharField(max_length=180, default="")
    uname = models.CharField(max_length=120, unique=True)
    upwd = models.CharField(max_length=180, unique=True)
    create_time = models.IntegerField(default=0)
    create_ip = models.CharField(max_length=40, default="")
    login_ip = models.CharField(max_length=40, default="")
    level = models.IntegerField(max_length=2, default=2)
    isno = models.IntegerField(max_length=2, default=0)
    plat_id = models.IntegerField(max_length=5, default=0)
    login_time = models.IntegerField(default=0)

    def __str__(self):
        return self.uname

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "管理员"
        verbose_name_plural = "管理员"
        db_table = "xys_admin"

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

# 订单表
class XinOrder(models.Model):

    number = models.IntegerField(max_length=20, default=0)
    shop_id = models.IntegerField(max_length=20, default=0)
    user_id = models.IntegerField(max_length=20, default=0)
    state = models.IntegerField(max_length=2, default=0)
    uname = models.CharField(max_length=100, default="")
    utel = models.CharField(max_length=60, default="")
    address = models.CharField(max_length=180, default="")
    money_ck = models.FloatField()
    create_time = models.IntegerField(max_length=10, default=0)
    target_time = models.IntegerField(max_length=10, default=0)
    shop_type = models.IntegerField(max_length=1, default=0)
    remark = models.CharField(max_length=180, default="")
    post_name = models.CharField(max_length=100, default="")
    post_number = models.CharField(max_length=100, default="")
    next_time = models.IntegerField(max_length=10, default=0)
    gettype = models.IntegerField(max_length=1, default=0)
    relation = models.CharField(max_length=20, default="")
    acctno = models.CharField(max_length=100, default="")
    phone = models.CharField(max_length=11, default="")
    del_time = models.IntegerField(max_length=11, default=0)
    week = models.IntegerField(max_length=1, default=0)
    is_prize = models.IntegerField(max_length=2, default=0)
    url_type = models.IntegerField(max_length=1, default=1)
    is_continue = models.IntegerField(max_length=1, default=0)
    year_hf = models.IntegerField(max_length=1, default=0)
    plat_id = models.IntegerField(max_length=10, default=0)
    end_time = models.IntegerField(max_length=10, default=0)
    is_now = models.IntegerField(max_length=1, default=0)
    beizhu = models.CharField(max_length=180, default="")
    award_id = models.IntegerField(max_length=10, default=0)
    card = models.CharField(max_length=40, default="")
    def __str__(self):
        return self.number
    class Meta:
        ordering = ["-create_time"]
        verbose_name = "订单表"
        verbose_name_plural = "订单表"
        db_table = "xys_xin_order"
    def to_dict(self):
        dict = {}
        dict['id'] = self.id
        dict['number'] = self.number
        dict['shop_id'] = self.shop_id
        dict['user_id'] = self.user_id
        dict['state'] = self.state
        dict['uname'] = self.uname
        dict['utel'] = self.utel
        dict['address'] = self.address
        dict['money_ck'] = self.money_ck
        dict['create_time'] = self.create_time
        dict['target_time'] = self.target_time
        dict['shop_type'] = self.shop_type
        dict['remark'] = self.remark
        dict['post_name'] = self.post_name
        dict['post_number'] = self.post_number
        dict['next_time'] = self.next_time
        dict['gettype'] = self.gettype
        dict['relation'] = self.relation
        dict['acctno'] = self.acctno
        dict['phone'] = self.phone
        dict['del_time'] = self.del_time
        dict['week'] = self.week
        dict['is_prize'] = self.is_prize
        dict['url_type'] = self.url_type
        dict['is_continue'] = self.is_continue
        dict['year_hf'] = self.year_hf
        dict['plat_id'] = self.plat_id
        dict['end_time'] = self.end_time
        dict['is_now'] = self.is_now
        dict['beizhu'] = self.beizhu
        dict['award_id'] = self.award_id
        dict['card'] = self.card
        return dict