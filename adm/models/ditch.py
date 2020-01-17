import time

from django.db import models


class Ditch(models.Model):
    name = models.CharField(max_length=60, unique=True)
    upper = models.FloatField(max_length=10, default=0)
    sole = models.CharField(max_length=60, default="")
    create_time = models.IntegerField(max_length=10, default=int(time.time()))
    del_time = models.IntegerField(max_length=10, default=0)
    type = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-create_time"]
        verbose_name = "平台表"
        verbose_name_plural = "平台表"
        db_table = "xys_wallet_ditch"

    def to_dict(self):
        dict = {}
        dict['id'] = self.id
        dict['name'] = self.name
        dict['upper'] = self.upper
        dict['sole'] = self.sole
        dict['create_time'] = self.create_time
        dict['del_time'] = self.del_time
        dict['type'] = self.type
        return dict