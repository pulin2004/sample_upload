#!/usr/bin/env python
# -*- coding:utf-8 -*-
from enum import Enum
fiedEnum = Enum('A', 'ant bee cat dog')


class FieldChange:

    def __init__(self):
        self.collumnName = ""

    def change(self,value):
        pass

 # 商派订单中每个字段对应的名称，分订单头和订单明细



class FieldChangeFactory:
    #所有对象对应值
    changes = {}