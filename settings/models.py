#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.db import models

class item(models.Model):
    shopex_item_code = models.CharField(max_length=100 ,unique = True ,db_index= True)
    kingdee_item_code = models.CharField(max_length=100)
    remark=models.CharField(max_length=200)
    pub_date = models.DateTimeField('发表时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField('更新时间', auto_now=True, null=True)

    def __str__(self):
        return self.shopex_item_code+" - "+self.kingdee_item_code
