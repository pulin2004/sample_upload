#!/usr/bin/env python
# -*- coding:utf-8 -*-

class BaseClass(object):
    def __init__(self):
        self._attrs = dict()
    def getAttr(self,attr):
        if self._attrs.has_key(attr):
            return self._attrs[attr]
        else:
            return None

    def setAttr(self,attr,newValue):
        if not self._attrs.has_key(attr):
            self._attrs[attr] =newValue
        else:
            _value = self.getAttr(attr)
            if _value != newValue:
                raise BaseException('订单(%s)的%s栏目的值不一致(%s,%s)'%(self._id,attr,_value,newValue),'views.py')

class Order(BaseClass):
    def __init__(self):
        BaseClass.__init__(self)
        self.details = []

    def dealLine(self, String):
        pass

    def addOrderDetai(self, OrderDetail):
        if any(OrderDetail):
            self.details.append()

class OrderDetail(BaseClass):
    def __init__(self):
        self._attrs = dict()

    def dealLine(self, String):
        pass    

