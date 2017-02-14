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


def enum(**enums):
    return type('Enum', (), enums)

#订单号,用户名,支付方式(payment),商品总额,配送费用,买家支付积分,订单总额,可得积分,已支付金额,买家实际支付积分,支付状态,订单附言,收货人姓名,收货地址,配送方式,电话,手机,下单日期,付款时间,
OrderEnum = enum(orderId='_id', consumer='_consumer',payment='_payment',totalAmount='_totalAmount',transportFee='_transportFee',accumulative='_accumulative',
               orderAmount='_orderAmount', raiseFen='_raiseFen',payed = '_payed',actualFen='_actualFen',payStatus='_payStatus',orderRemark='_orderRemark',receiverName='_receiverName',receiverAddr='_receiverAddr',shipping='_shipping',phone='_phone',mobliePhone='_mobliePhone',orderDate='_orderDate',payDate='_payDate')
#商品名称,宝贝种类,发货单号,物流公司,订单备注
OrderDetalEnum = enum(productName='_productName',productType='_productType',shippingNum='_shippingNum',shippinCompany='_shippingCompany',orderRemark='_orderRemark')
# Numbers.ONE == 1, Numbers.TWO == 2 and Numbers.THREE == 'three'