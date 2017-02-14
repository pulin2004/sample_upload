#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

from django.http import HttpResponseRedirect
from django.shortcuts import render
import fileUtils
import csv
import time
import random
import upload.order

from upload.order import Order

suffixType = ('csv');


# 表单
def index(request):
    print("upload index new1!")
    return render(request, 'upload2.html')


def upload_file(request):
    print("start upload file!")
    if request.method == "POST":  # 请求方法为POST时，进行处理ok
        myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return render(request, 'message.html', {"message": "上传失败!", "message_detail": "没有上传文件！"})
        sufix = fileUtils.getSufix(myFile.name)
        if not fileUtils.isSameType(sufix,suffixType):
            return render(request, 'message.html', {"message": "上传失败!", "message_detail": "不能解析%s文件！" % {sufix}})
        first = True
        orders=dict()
        messageInfo = MessageInfo()
        reader = csv.reader(myFile)
        for line in reader:
            if first:
                first = False
            else:
                deal_line(line,orders,messageInfo)
        if messageInfo.isSuccess():
            downPath = 'kingdee_'+time.strftime('%Y%m%d-%H:%M:%S',time.localtime(time.time()))+'_'+str(random.randint(100,999))
            wirteKingdeefile(orders,downPath)
            return render(request, 'down.html', {"message": "上传成功!", "message_detail": messageInfo.getMessage(),"down_link":downPath})
        else:
            return render(request, 'errormessage.html',{"message": "处理失败!", "message_detail": messageInfo.getMessage()})
    else:
        return HttpResponseRedirect('/')


def deal_line(line,orders,messageInfo):
    if not line[0]:
        return
    _id = line[0]
    _order = getOrder(orders,_id)
    _order.setAttr('client_name',line[1])
    if _order._id:
        pass
                      


def getOrder(orders,_id):
    if not orders.has_key(_id):
        orders[_id]=Order()
        orders[_id]._id = _id
    return orders[_id]

def wirteKingdeefile(orders,path):
    pass

class MessageInfo:
    def __init__(self):
        self.__flag = True
        self.__message ={}

    def isSuccess(self):
        return self.__flag

    def getMessage(self):
        return self.__message

    def addMessage(self,status,lineNu,message):
        if not status:
            self.__flag =False
        self.__message.update({lineNu:str(message)})
