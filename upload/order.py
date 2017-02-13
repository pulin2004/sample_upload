#!/usr/bin/env python
# -*- coding:utf-8 -*-



class Order:
    def __init__(self):
        self.details = []

    def dealLine(self, String):
        pass

    def addOrderDetai(self, OrderDetail):
        if any(OrderDetail):
            self.details.append()

    def compareAndWriteAttr(self,attr,newVaule):
        _value = getattr(self,attr)
        if _value:
            setattr(self,attr,newVaule)
        elif _value != newVaule:
            raise VauleError('订单(%s)的%s栏目的值不一致(%s,%s)'%(self._id,attr,_value,newValue),'views.py')



class OrderDetail:
    def dealLine(self, String):
        pass

